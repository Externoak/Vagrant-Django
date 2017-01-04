from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nmap/$', views.nmap, name='nmap'),
    url(r'^speedtest/$', views.speedtest, name='speedtest'),
    url(r'^main/$', views.main, name='main'),
    url(r'^dependencies/$', views.dependencies, name='dependencies'),
    url(r'^pingcheck/$', views.pingcheck, name='pingcheck'),
    url(r'^webstatus/$', views.webstatus, name='webstatus'),
]
