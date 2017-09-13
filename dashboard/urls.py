from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accept-invite$', views.accept_invite, name='accept-invite'),
    url(r'^decline-invite$', views.decline_invite, name='decline-invite'),
    url(r'^edit-profile$', views.edit_profile, name='edit-profile')
]
