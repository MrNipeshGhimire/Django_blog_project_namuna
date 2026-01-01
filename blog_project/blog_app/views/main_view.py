from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ..models import Blogs
from django.contrib import messages


def index_page(request):
    return render(request,'main/index.html')


def about_page(request):
    return render(request,'main/about_page.html')

@login_required
def create_blog(request):
    errors = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        description = request.POST.get('description')

        if not title:
            errors['title'] = "Title is Required"
        
        if errors:
            return render(request,'main/create_blog.html',{'errors':errors,'data':request.POST})
        
        try:
            # try
            blog = Blogs.objects.create(
                title=title,
                category=category,
                description=description,
                image=image,
                author = request.user
            )
            blog.save()
            messages.success(request,"Blog posted successfully !! ")
            return redirect('index')

        except Exception as e:
            print(f"Error occurs :{e}")
            return render(request,'main/create_blog.html',{'errors':"Failed to add blog"})
    return render(request,'main/create_blog.html')