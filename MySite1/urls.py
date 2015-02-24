from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    #Examples:
    #url(r'^$', 'MySite1.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/login/$', 'django.contrib.auth.views.login', {'templates_name': 'login.html'}),
    url(r'^users/logout/$', 'django.contrib.auth.views.logout', {'templates_name': 'home.html'}),
    url(r'^users/account/$', 'polls.views.user_account', name='useraccount'),
    url(r'^users/account/$', 'polls.views.user_home', name='userhome')


    )