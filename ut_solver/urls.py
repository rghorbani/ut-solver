from django.conf.urls import patterns, include, url
from django.contrib import admin
# from django.conf.urls.defaults import handler404, handler500, handler403

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ut_solver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'solver_frontend.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^problem/', 'ut_solver.views.problem', name='problem'),
    url(r'^problem/(?P<problem_id>\d+)/view', 'ut_solver.views.problem_view', name='view_problem'),

    url(r'^users/sign_in/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^users/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
)

# handler404 = "solver_frontend.views.handler404"
# handler500 = "solver_frontend.views.handler500"
# handler403 = "solver_frontend.views.handler403"