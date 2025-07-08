from django.shortcuts import redirect,render
from ..models import Blog


def index(request):
    return render(request,'main/index.html')


def create_blog(request):
    errors = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        
        if not title:
            errors['title'] = "Title is required"
        
        if not category:
            errors['category'] = "Category is required"
        
        if not description:
            errors['description'] = "Description is required"
        
        if not image:
            errors['image'] = "Image field is required"
        
        if errors:
            return render(request,'main/create_blog.html',{'errors':errors,'data':request.POST})
        
        Blog.objects.create(
            title=title,
            category = category,
            description = description,
            image = image,
            author = request.user
        )
        return redirect('index')
        # return render(request,'main/create_blog.html',{'message':"Blog posted Successfully"})
        # Blog(title=title, category=category, description=description)
        # Blog.save()
        
    else:   
        return render(request,'main/create_blog.html')
    




