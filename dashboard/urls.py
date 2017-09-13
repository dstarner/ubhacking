from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit-profile$', views.edit_profile, name='edit-profile')
]
