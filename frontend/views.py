from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages

from frontend.forms import *
from frontend.tasks import *

# %matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.path import Path
# from matplotlib import get_current_fig_manager
import matplotlib.patches as patches
from mpld3 import fig_to_html, plugins
from ut_solver.settings import STATIC_URL
from lex.lexer import solve_p


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

    # fig, ax = plt.subplots()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    vertics = [
        (1, 1),
        (1, 2),
        (2, 2),
        (2, 1),
        (1, 1),
    ]
    codes = [
        Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,
    ]
    path = Path(vertics, codes)
    patch = patches.PathPatch(path, facecolor='orange', lw=2)
    ax.add_patch(patch)
    ax.set_xlim(-1, 3)
    ax.set_ylim(-1, 3)
    xs, ys = zip(*vertics)
    ax.plot(xs, ys, 'x-', lw=2, color='black', ms=10)
    ax.plot([2, 0], [0, 2], 'k--', lw=1)
    ax.plot([0], [0], 'w,', lw=1)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_title('2D Plot of the Problem!', size=14)
    plugins.clear(fig)
    plugins.connect(fig, plugins.Reset(), plugins.Zoom(enabled=True), plugins.BoxZoom())
    figure = fig_to_html(fig, d3_url=STATIC_URL + 'js/d3.min.js', mpld3_url=STATIC_URL + 'js/mpld3.v0.2.js', use_http=True)

    # calc = solve_p()
    # res = calc(problem.problem_text)
    a, b, c = solve_p(problem.problem_text)

    return render_to_response('problems/view.html', {
        'user': user,
        'problem': problem,
        'figure': figure,
        'a': a,
        'b': b,
        'c': c,
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