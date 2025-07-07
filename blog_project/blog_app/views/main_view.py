from django.shortcuts import redirect,render


def index(request):
    return render(request,'main/index.html',{'user':request.user})

def create_blog(request):
    return render(request,'main/create_blog.html')