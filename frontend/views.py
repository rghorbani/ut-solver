from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# from django.contrib import messages

from frontend.forms import *
from frontend.tasks import *

# %matplotlib inline
import copy
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.path import Path
# from matplotlib import get_current_fig_manager
import matplotlib.patches as patches
from mpld3 import fig_to_html, plugins
from ut_solver.settings import STATIC_URL, BASE_DIR
from lex.lexer import parse_problem
from lexer.parser import parsing_cuda
from simplex.cuda.cuda import solving_cuda
import os.path



def index(request):
    user = request.user
    if user is None:
        return render(request, "home/index.html", {})
    else:
        return render_to_response("home/index.html", {
            'user': user,
            'is_admin': user.has_perm('admin'),
        })


def user_register(request):
    if request.user.is_authenticated():
        return redirect('/')
    form = UserCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        new_user = form.save()
        new_user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, new_user)
        # messages.success(request, 'Logged in Successfully.')
        return index(request)
    else:
        return render_to_response('users/register.html', {
            'form': form,
            'view_name': 'Register',
        }, context_instance=RequestContext(request))


@login_required
def user_profile(request):
    user = request.user
    form = UserProfileForm(request.POST or None, instance=user)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/')
    else:
        return render_to_response('users/profile.html', {
            'form': form,
            'view_name': 'Edit Profile',
        }, context_instance=RequestContext(request))


@login_required
def problem_index(request):
    user = request.user
    if user.is_superuser:
        problems = Problem.objects.all().order_by('-created_at')
    else:
        problems = Problem.objects.filter(user_id=user.id).order_by('-created_at')
    return render_to_response('problems/index.html', {
        'user': user,
        'problems': problems,
        'view_name': 'Problems',
        'is_admin': user.is_superuser,
    })


@login_required
def problem_new(request):
    form = NewProblemForm(request.POST or None)
    return render_to_response('problems/new.html', {
        'user': request.user,
        'view_name': 'New Problem',
        'form': form,
    }, context_instance=RequestContext(request))


@login_required
def problem_create(request):
    if request.method == 'POST':
        form = NewProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user_id = request.user
            problem.save()
            solve_problem.delay(problem)
            return redirect('/problems/%s/view' % problem.id)
        else:
            return problem_new(request)
    else:
        return redirect('/problems/new')


@login_required
def problem_view(request, problem_id):
    user = request.user
    problem = get_object_or_404(Problem, id=problem_id)
    if problem.user_id != user and not user.is_superuser:
        raise PermissionDenied

    parse_error = False
    a = None
    b = None
    c = None
    a_copy = None
    b_copy = None
    result = None
    figure = None
    parse_result = parse_problem(problem.problem_text)
    print parse_result
    if parse_result is not None:
        a, b, c, x = parse_result
        if a and b and c and x:
            result = simple_simplex(copy.deepcopy(a), copy.deepcopy(b), copy.deepcopy(c))
            b.pop(0)
            a_copy = copy.deepcopy(a)
            b_copy = copy.deepcopy(b)

            if len(x) is 2:
                tmp = [0, 0]
                tmp[1] = 1
                a.insert(0, copy.deepcopy(tmp))
                tmp[0] = 1
                tmp[1] = 0
                a.insert(0, copy.deepcopy(tmp))
                b.insert(0, 0)
                b.insert(0, 0)
                dots = []
                for i in range(len(b)):
                    dots.append([])
                shape_x = []
                for i in xrange(0, len(b)):
                    for j in xrange(i + 1, len(b)):
                        if a[i][0] == a[j][0] and a[i][1] == a[j][1]:
                            continue
                        shape_a = np.array([[a[i][0], a[i][1]], [a[j][0], a[j][1]]])
                        shape_b = np.array([b[i], b[j]])
                        res = np.linalg.solve(shape_a, shape_b)
                        dots[i].append(res)
                        dots[j].append(res)
                # fig, ax = plt.subplots()
                fig = plt.figure()
                ax = fig.add_subplot(111)
                for dot in dots:
                    ax.plot([float(dot[0][0]), float(dot[1][0])], [float(dot[0][1]), float(dot[1][1])], ls='-', color='green', marker='o', lw=2)
                    # print([dot[0], dot[1]])
                ax.set_xlabel('X axis')
                ax.set_ylabel('Y axis')
                ax.set_title('Plot of 2D Problem!', size=14)
                plugins.clear(fig)
                plugins.connect(fig, plugins.Reset(), plugins.Zoom(enabled=True), plugins.BoxZoom())
                figure = fig_to_html(fig, d3_url=STATIC_URL + 'js/d3.min.js', mpld3_url=STATIC_URL + 'js/mpld3.v0.2.js', use_http=True)
            else:
                figure = 'Larger than 2D!'
    else:
        parse_error = True

    return render_to_response('problems/view.html', {
        'user': user,
        'problem': problem,
        'parse_error': parse_error,
        'figure': figure,
        'a': a_copy,
        'b': b_copy,
        'c': c,
        'result': result,
        'view_name': 'Problem - %s' % problem.id,
    })


@login_required
def problem_edit(request, problem_id):
    user = request.user
    if not user.is_superuser:
        raise PermissionDenied
    problem = get_object_or_404(Problem, id=problem_id)
    form = NewProblemForm(request.POST or problem)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/problems')
    else:
        return render_to_response('problems/edit.html', {
            'user': user,
            'form': form,
            'view_name': 'Edit Problem - %s' % problem.id,
        }, context_instance=RequestContext(request))


@login_required
def problem_delete(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    if problem.user_id == request.user:
        problem.delete()
        redirect('/problems')
    else:
        raise PermissionDenied()


def handle_uploaded_file(f):
    with open(BASE_DIR + '/cuda.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@login_required
def problem_cuda(request):
    user = request.user
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            redirect('/problem/cuda')
    else:
        form = UploadFileForm()
    form2 = SolveCudaForm()
    file_exists = os.path.exists(BASE_DIR + '/cuda.txt')
    return render_to_response('problems/cuda.html', {
        'user': user,
        'form': form,
        'form2': form2,
        'file_exists': file_exists,
        'view_name': 'Problem - CUDA',
    }, context_instance=RequestContext(request))


@login_required
def parse_cuda(request):
    user = request.user
    parsing_cuda()
    form = UploadFileForm()
    form2 = SolveCudaForm()
    file_exists = os.path.exists(BASE_DIR + '/cuda.txt')
    return render_to_response('problems/cuda.html', {
        'user': user,
        'form': form,
        'form2': form2,
        'file_exists': file_exists,
        'view_name': 'Problem - CUDA',
    }, context_instance=RequestContext(request))


@login_required
def solve_cuda(request):
    user = request.user
    form = SolveCudaForm(request.POST)
    if form.is_valid():
        maximum = False
        if form.cleaned_data['choice'] == 'max':
            maximum = True
        result = solving_cuda(maximum)
        return render_to_response('problems/cuda_result.html', {
            'user': user,
            'result': result,
            'view_name': 'Problem - CUDA - Result',
        })
    else:
        form = UploadFileForm()
        form2 = SolveCudaForm()
        file_exists = os.path.exists(BASE_DIR + '/cuda.txt')
        return render_to_response('problems/cuda.html', {
            'user': user,
            'form': form,
            'form2': form2,
            'file_exists': file_exists,
            'view_name': 'Problem - CUDA',
        })


def handler403(request):
    message = "403! You Don't have permission to access this page!"
    return render_to_response('error.html', {
        'user': request.user,
        'message': message,
        'view_name': '403',
    })


def handler404(request):
    message = "404! The page you requested was not found!"
    return render_to_response('error.html', {
        'user': request.user,
        'message': message,
        'view_name': '404',
    })


def handler500(request):
    message = "500! Something went wrong with our server. We are sorry!"
    return render_to_response('error.html', {
        'user': request.user,
        'message': message,
        'view_name': '500',
    })