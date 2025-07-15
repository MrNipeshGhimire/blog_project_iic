from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# def login_page(request):
#     errors = {}
#     if request.method == 'POST':
#         # username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         if not email:
#             errors['email'] = "Email is required"
#         elif not User.objects.filter(email=email).exists():
#             errors['email'] = "Email does not exist | Incorrect Email"
        
#         if not password:
#             errors['password'] = "Password is required"
        
#         if errors:
#             return render(request,'auth/login_page.html',{'errors':errors, 'data':request.POST})
        
#         auth_user = User.objects.get(email=email) # select * from User where email=email
#             user = authenticate(request,username=auth_user.username,password=password) # 
#             if user is not None:
#                 login(request,user)   # session generate garxa
#                 messages.success(request,"Login Successful")
#                 return redirect('index')
#         except:
#             errors['password'] = "Incorrect Password"
#             return render(request,'auth/login_page.html',{'errors':errors,'data':request.POST})
#     return render(request,'auth/login_page.html')


def login_page(request):
    errors ={}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email:
            errors['email'] = 'Email is required'
        elif not User.objects.filter(email=email).exists():
            errors['email'] = 'Email does not exist | Incorrect Email'
        
        if not password:
            errors['password'] = 'Password is required'
        
        if errors:
            return render(request,'auth/login_page.html',{'errors':errors,'data':request.POST})
        
        auth_user = User.objects.get(email=email)  #get user object
        user = authenticate(request,username=auth_user.username, password=password)
        if user is not None:
            login(request,user) # session generate hunxa
            messages.success(request,'Login Successful')
            return redirect('index')
        else:
            errors['password'] = 'Incorrect Password'
            return render(request,'auth/login_page.html',{'errors':errors,'data':request.POST})
    return render(request,'auth/login_page.html')

def register_page(request):
    errors = {}     
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if not password:
            errors['password'] = "Password field is required"
        
        if not confirm_password:
            errors['confirm_password'] = "This field also required"
        
        if password != confirm_password:
            errors['confirm_password'] = "Password and confirm password does not matched"
        
        if not username:
            errors['username'] = "Username field is required"
        
        if not email:
            errors['email'] = "Email field is required"
        
        if not errors:
            # user = User.objects.create(
            #     username=username,
            #     email = email
            # )
            # user.set_password(password) # hash => encrypted
            # user.save()
            user = User.objects.create_user(
                username=username,
                email = email,
                password=password
            )
            user.save()
            return redirect('login')
        else:
            errors['error'] = "Failed to Register"
            return render(request,'auth/register_page.html',{'errors':errors,'data':request.POST})
                   
    return render(request,'auth/register_page.html')

def logout_user(request):
    logout(request)
    return redirect('index')
    


def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    errors = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        if not username:
            errors['username'] = "Username is required"
        
        
        if not email:
            errors['email'] = "Email is required"
        
        if errors:
            return render(request,'auth/user_profile.html',{'errors':errors})
        # try:
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        print(user.username, user.email, user.first_name, user.last_name)
        user.save()
        messages.success(request,'Profile updated successfully')
        return render(request,'auth/user_profile.html',{'message':"Profile Updated Successfully"})
       
    return render(request,'auth/user_profile.html',{'user':user})

def change_password(request, user_id):
    return render(request,'auth/change_password.html')