from django.urls import path
from . import views

# from .views import logout_user
# from .views import login_portal


urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
     path('contact/', views.contact_view, name='contact'),
    path('news/', views.news_list, name='news'),
    path('events/', views.events_view, name='events'),
    path('gallery/', views.gallery, name='gallery'),
    path('leadership/', views.leadership_team, name='leadership'),
    path('register/', views.register_view, name='register'),
    path('donate/', views.donate_view, name='donate'),
    # Add these to your existing URL patterns
    path('login_portal/', views.login_portal, name='login_portal'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # path('logout/', logout_user, name='login_portal')


]
