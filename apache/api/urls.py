from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CreateView, DetailsView, UserView, UserDetailsView

# Create urls here.

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get-token/', obtain_auth_token),
    url(r'^complaints/$', CreateView.as_view(), name="create"),
    url(r'^complaints/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailsView.as_view(), name="user_details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
