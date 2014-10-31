from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from frontend.models import *
from frontend.forms import *


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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, 'Logged in Successfully.')
            return index(request)
        else:
            return redirect('/users/sign_up')
    else:
        form = UserCreationForm()
        return render_to_response('users/register.html', {
            'form': form,
            'view_name': 'Register',
        }, context_instance=RequestContext(request))


@login_required
def user_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, 'Profile updated Successfully.')
            return index(request)
    else:
        form = UserCreationForm()
        return render_to_response('users/profile.html', {
            'user': user,
            'form': form,
            'view_name': 'Register',
        }, context_instance=RequestContext(request))


@login_required
def problem_index(request):
    user = request.user
    problems = Problem.objects.filter(user_id=user.id).order_by('-created_at')
    return render_to_response('problems/index.html', {
        'user': user,
        'problems': problems,
        'view_name': 'Problems',
    })


@login_required
def problem_new(request):
    form = NewProblemForm()
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
            return HttpResponseRedirect('/problems/%s/view' % problem.id)
        else:
            return problem_new(request)
    else:
        return redirect('/problems/new')


@login_required
def problem_view(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    return render_to_response('problems/view.html', {
        'user': request.user,
        'problem': problem,
        'view_name': 'Problem - %s' % problem.id,
    })


@login_required
def problem_delete(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    if problem.user_id == request.user.id:
        problem.delete()
        redirect('/problems')
    else:
        raise PermissionDenied()


def handler403(request):
    message = "403! You Don't have permission to access this page!"
    return render_to_response('error.html', {
        'message': message,
        'view_name': '403',
    })


def handler404(request):
    message = "404! The page you requested was not found!"
    return render_to_response('error.html', {
        'message': message,
        'view_name': '404',
    })


def handler500(request):
    message = "500! Something went wrong with our server. We are sorry!"
    return render_to_response('error.html', {
        'message': message,
        'view_name': '500',
    })