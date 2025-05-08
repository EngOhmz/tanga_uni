from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('news/', views.news_list, name='news'),
    path('events/', views.events_list, name='events'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('leadership/', views.leadership_team, name='leadership'),
    path('register/', views.register_view, name='register'),
    path('donate/', views.donate_view, name='donate'),
]
