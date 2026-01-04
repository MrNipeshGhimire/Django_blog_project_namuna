from django.urls import path
from .views.main_view import index_page,about_page,create_blog,single_method
from .views.auth_view import login_method, register_method,logout_method


urlpatterns = [
    path('',index_page, name="index"),
    path('about/',about_page, name="about"),
    path('login/',login_method, name="login"),
    path('register/',register_method, name="register"),
    path('logout/',logout_method, name="logout"),
    path('create/',create_blog, name="create"),
    path('single/<int:id>/',single_method, name="single")
]

