from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from solver_frontend.models import Problem


def index(request):
    if not request.session.has_key('auth_user_id'):
        return render(request, 'home/index.html', {})
    user_id = request.session['_auth_user_id']
    user = User.objects.get(id=user_id)
    return render_to_response('home.index.html', {
        'user': user,
        'is_admin': user.has_perm('admin'),
    })


@login_required
def problem(request):
    user = request.user
    return render_to_response('problem/index.html', {
        'user': user,
    })


@login_required
def problem_view(request, problem_id):
    user = request.user
    problem = Problem.objects.get(id=problem_id)
    return render_to_response('problem/view.html', {
        'user': user,
        'problem': problem,
    })


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