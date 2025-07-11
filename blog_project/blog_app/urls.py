from django.urls import path
from .views.auth_view import login_page,register_page,logout_user
from .views.main_view import index,create_blog,single_page,edit_blog

urlpatterns = [
    path('login/',login_page, name="login"),
    path('register/',register_page, name="register"),
    path('',index, name="index"),
    path('logout/',logout_user, name="logout"),
    path('create/',create_blog, name="create"),
    path('single/<int:id>',single_page, name="single"),
    path('edit/<int:id>',edit_blog, name="edit")   
    
]
