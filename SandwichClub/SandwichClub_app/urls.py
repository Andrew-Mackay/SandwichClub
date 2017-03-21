from django.conf.urls import url
from SandwichClub_app import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	#url(r'^profile/', views.profile, name='profile'),
	url(r'^about/', views.about, name='about'),
    url(r'^more/', views.more, name='more'),
    url(r'^contact/', views.contact, name='contact'),
        url(r'^search/$', views.search, name='search'),
        url(r'^random/$', views.randomsando),
        url(r'^top_ten/$', views.top_ten, name='top_ten'),
        url(r'^latest/$', views.latest, name='latest'),
	#url(r'^register_profile/$', views.register_profile, name='register_profile'),
	url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
	url(r'^create_sandwich/$', views.create_sandwich, name='create_sandwich'),
	url(r'^sandwich/(?P<sid>[\w\-]+)$', views.sandwich, name='sandwich'),
]
