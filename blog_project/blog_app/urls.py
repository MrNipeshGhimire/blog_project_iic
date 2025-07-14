from django.urls import path
from .views.auth_view import login_page,register_page,logout_user,user_profile,change_password
from .views.main_view import index,create_blog,single_page,edit_blog,delete_blog

urlpatterns = [
    path('login/',login_page, name="login"),
    path('register/',register_page, name="register"),
    path('',index, name="index"),
    path('logout/',logout_user, name="logout"),
    path('create/',create_blog, name="create"),
    path('single/<int:id>',single_page, name="single"),
    path('edit/<int:id>',edit_blog, name="edit") ,
    path('delete/<int:blog_id>',delete_blog, name="delete"),
    path('profile/<int:user_id>',user_profile, name="profile"),
    path('change_password/<int:user_id>',change_password, name="change_password")
    
]

# http://127.0.0.1:8000/blog    # POST, GET
# http://127.0.0.1:8000/blog/5   # GET,PUT, DELETE

