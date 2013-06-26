from django.conf.urls import patterns, include, url
from django.contrib import admin

from entries.views import EntryListView, EntryCreateView, EntryUpdateView, EntryDetailView
from users.views import UserCreateView, UserUpdateView, UserDetailView, UserListView

admin.autodiscover()

urlpatterns = patterns('',

	url(r'^users/$', UserListView.as_view(), name="user_list"),
	url(r'^users/(?P<pk>\d+)$', UserDetailView.as_view(), name="user_detail"),
	url(r'^users/create/$', UserCreateView.as_view(), name="users_create"),
	url(r'^users/update/(?P<pk>\d+)/$', UserUpdateView.as_view(), name="users_update"),

	url(r'^$', EntryListView.as_view(), name='entries_list'),
	url(r'^create/$', EntryCreateView.as_view(), name='entries-create'),
	url(r'^update/(?P<pk>\d+)/$', EntryUpdateView.as_view(), name='entries-update'),
	url(r'^detail/(?P<pk>\d+)/$', EntryDetailView.as_view(), name='entry_detail'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
