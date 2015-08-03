from django.conf.urls import patterns, include, url
from login.views import login_user, saveStudent, saveTeacher, getStudents
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^login/$', login_user),
    url(r'^registerStudent/$', saveStudent),
    url(r'^registerTeacher/$', saveTeacher),
    url(r'^getStudents/$', getStudents),
    url(r'^admin/', include(admin.site.urls)),
)
