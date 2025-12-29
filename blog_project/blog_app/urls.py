from django.urls import path
from .views.main_view import index_page,about_page
from .views.auth_view import login_method, register_method


urlpatterns = [
    path('',index_page, name="index"),
    path('about/',about_page, name="about"),
    path('login/',login_method, name="login"),
    path('register/',register_method, name="register")
]

