from django .urls import path 
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('contact', views.contact, name='contact'),
    path('menu', views.menu, name='menu'),
    path('services', views.services, name='services'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signup', views.signup, name='signup'),
]
