from django.conf.urls import patterns, include, url
from django.contrib import admin
# from django.conf.urls.defaults import handler404, handler500, handler403

urlpatterns = patterns('',
    url(r'^', include('solver_frontend.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

handler404 = "solver_frontend.views.handler404"
handler500 = "solver_frontend.views.handler500"
handler403 = "solver_frontend.views.handler403"