from django.conf.urls import patterns, url
from timey import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
)