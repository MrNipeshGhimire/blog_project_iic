from django.shortcuts import redirect,render, get_object_or_404
from ..models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    blog = Blog.objects.all()
    # if not blog:
    #     return render(request,'main/index.html',{'message':"No blogs Available"})
    return render(request,'main/index.html',{'blog':blog})


@login_required
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


def single_page(request, id): 
    # blog = Blog.objects.get(id=id)
    blog = get_object_or_404(Blog, id=id)
    # print(blog)
    return render(request,'main/single_page.html',{'blog':blog})

# def edit_blog(request, id ):
#     blog = get_object_or_404(Blog, id=id)
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         category = request.POST.get('category')
#         image = request.FILES.get('image')
#         description = request.POST.get('description')   # 1    # 4
        
#         if blog.author != request.user:
#             return redirect('single',id=blog.id)
#         else:       
#             blog.title = title
#             blog.image = image
#             blog.category = category
#             blog.description = description
#             blog.save()
#             return redirect('single', id=blog.id)
    
#     return render(request,'main/edit_blog.html',{'blog':blog})


def edit_blog(request, id):
    previous_data = Blog.objects.get(id=id) 
    print(previous_data.author)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        
        if previous_data.author == request.user:
            previous_data.title = title
            previous_data.category = category
            previous_data.description = description
            if image:
                previous_data.image = image
            previous_data.save()
            return redirect('single',id=previous_data.id) 
        else:
            messages.error(request,'You are not authorized to edit this Blog')
            return redirect('single',id=previous_data.id) 
                
    # if previous_data.author == request.user:
        
        
    return render(request,'main/edit_blog.html',{'blog':previous_data})
    

