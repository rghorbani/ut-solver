from django.conf.urls import patterns, url
from frontend import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^problems/$', views.problem_index, name='problems'),
    url(r'^problems/new', views.problem_new, name='new_problem'),
    url(r'^problems/create', views.problem_create, name='create_problem'),
    url(r'^problems/(?P<problem_id>\d+)/view/$', views.problem_view, name='view_problem'),

    url(r'^users/sign_up', views.user_register, name='register'),
    url(r'^users/sign_in/$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}),
    url(r'^users/sign_out/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    # url(r'^users/', include('django.contrib.auth.urls')),
)