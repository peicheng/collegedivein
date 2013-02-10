from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from event.views import EventListView, EventTypeListView, EventDetailView

urlpatterns = patterns('',
    # url(r'^$', 'cdi.views.home', name='home'),
    url(r'^$', EventListView.as_view(), name='event_all'),
    url(r'^type/(?P<pk>\d+)/$', EventTypeListView.as_view(), name='event_types'),
    url(r'^(?P<pk>\d+)/$', login_required(EventDetailView.as_view()), name='event_detail'),
    )