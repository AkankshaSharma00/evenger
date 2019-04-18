from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from rest_framework import views
# from django.views.generic.simple import direct_to_template


from . import views

urlpatterns=[
	url(r'^index/$',views.IndexView.as_view(),name='index'),
	url(r'^(?P<polls_id>\d+)/$',views.DetailView.as_view(),name='detail'),
	# url('<int:pk>/',views.DetailView.as_view(),name="detail"),
	url(r'^(?P<polls_id>\d+)/results/',views.ResultsView.as_view(),name='results'),
	url(r'^(?P<polls_id>\d+)/vote/',views.vote,name='vote'),
]