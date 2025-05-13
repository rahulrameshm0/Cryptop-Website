from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home, name='home'), 
    path('about/',views.about, name='about'),
    path('how/',views.how, name='how'),
    path('login/',views.login_account, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.signup_account, name='register'),
]