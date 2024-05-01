from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^folders/$', views.folders, name='folders'),
	url(r'^folder/(?P<folder_id>\d+)/$', views.folder, name='folder'),
	url(r'new_folder/$', views.new_folder, name='new_folder'),
	url(r'upload/(?P<folder_id>\d+)/$', views.upload, name='upload'),
]