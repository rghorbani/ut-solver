from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from solver_frontend.models import Problem


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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect('/problems')
    else:
        form = UserCreationForm()
        return render_to_response('users/register.html', {
            'form': form,
        })

@login_required
def problem_index(request):
    user = request.user
    problems = Problem.objects.filter(user_id=user.id).order_by('-created_at')
    return render_to_response('problems/index.html', {
        'user': user,
        'problems': problems,
    })


@login_required
def problem_new(request):
    return render_to_response('problems/new.html', {
        'user': request.user,
    })


@login_required
def problem_create(request):
    if request.method == 'POST':
        return redirect('problem/view')
    else:
        return redirect('/problem/new')


@login_required
def problem_view(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    return render_to_response('problems/view.html', {
        'user': request.user,
        'problem': problem,
    })


@login_required
def problem_delete(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    if problem.user_id == request.user.id:
        problem.delete()
    else:
        raise handler403(request)


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