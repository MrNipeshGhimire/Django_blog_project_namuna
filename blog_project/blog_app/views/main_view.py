from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Blogs
from django.contrib import messages


def index_page(request):
    try:
        blog = Blogs.objects.only('title','category','image','created_at')  # select title,category,image,created_at from Blog 
        print(blog)
        return render(request,'main/index.html',{'blog':blog})
    
    except Exception as e:
        print(f"error: {e}")

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

# for single blog display
def single_method(request,id):
    try:
        blog = get_object_or_404(Blogs,id=id)   # select * from Blogs where id=id
        # blog = Blogs.objects.get(id=id)
        print(blog)
        return render(request,'main/single_blog.html',{'blog':blog})
    except Exception as e:
        print("Error: ",e)
    return render(request,'main/single_blog.html')