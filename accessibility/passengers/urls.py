from django.conf.urls import url

from . import views

app_name = 'passengers'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'waiting', views.waiting, name='waiting'),
	url(r'onboard', views.onboard, name='onboard'),
	]