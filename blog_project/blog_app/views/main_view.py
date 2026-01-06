from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Blogs
from django.contrib import messages


def index_page(request):
    try:
        blog = Blogs.objects.only('title','category','image','created_at').order_by('-created_at')  # select title,category,image,created_at from Blog 
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

# for deleting blog
@login_required
def delete_blog(request,pk):
    try:
        blog =  Blogs.objects.get(id=pk)
        # get_object_or_404(Blogs,id=pk)
        if blog.author == request.user:
            blog.delete()
            messages.success(request,'Blog deleted successfully')
            return redirect('index')
        else:
            return render(request,'main/single_blog.html',{'error':"You are not authorized to delete this blog",'blog':blog})
    except Exception as e:
        print(e)


# edit 
def edit_method(request,id):
    error={}
    prev_blog = get_object_or_404(Blogs,id=id)

    if prev_blog.author != request.user:
        return redirect('single', prev_blog.id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        description = request.POST.get('description')

        if not title:
            error['title'] = "Title is required"

        if not category:
            error['category'] = "Category is required"
        
        if not description:
            error['description'] = "Description is required"

        if error:
            return render(request,'main/edit_blog.html',{'prev_blog':prev_blog,'error':error})
        
        # edit 
        prev_blog.title = title
        prev_blog.category = category
        if image:
            prev_blog.image = image
        prev_blog.description = description
        prev_blog.save()
        messages.success(request,'Blog updated successfully')
        return redirect('single',id=prev_blog.id)

    return render(request,'main/edit_blog.html',{'prev_blog':prev_blog})