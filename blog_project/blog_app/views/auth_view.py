from django.shortcuts import render,redirect
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
    
