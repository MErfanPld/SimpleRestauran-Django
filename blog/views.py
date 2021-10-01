from django.shortcuts import render
from .models import Blog, Tag, Category, Comments
from .forms import CommetForm

# Create your views here.

#==============================blog_list==============================#

def blog_list(request):
    blog_list = Blog.objects.all()

    context = {
        "blog_list": blog_list,
    }
    return render(request, "blogs/blog_list.html", context)

#==============================blog_detail==============================#

def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    tags = Tag.objects.all().filter(blogs=blog)
    recents = Blog.objects.all().order_by("-created_at")
    Categories = Category.objects.all()
    comments = Comments.objects.all().filter(blog=blog)

    if request.method == "POST":
        form = CommetForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data["fullname"]
            email = form.cleaned_data["email"]
            massage = form.cleaned_data["massage"]
            new_comment = Comments(blog=blog, fullname=fullname, email=email, massage=massage)
            new_comment.save()

    context = {
        "blog": blog,
        "tags": tags,
        "recents": recents,
        "Categories": Categories,
        "comments": comments,
    }
    return render(request, "blogs/blog_detail.html", context)

#==============================blog_tag==============================#

def blog_tag(request,tag):
    blog_list = Blog.objects.filter(tags__slug=tag)
    context = {
        "blog_list": blog_list
    }
    return render(request, "blogs/blog_list.html", context)

#==============================blog_category==============================#

def blog_category(request, category):
    blog_list = Blog.objects.filter(category__slug=category)
    context = {
        "blog_list": blog_list
    }
    return render(request, "blogs/blog_list.html", context)

#==============================blog_Search==============================#

def Search(request):
    if request.method == "GET":
        q = request.GET.get("search")
    blog_list = Blog.objects.filter(title__icontains=q)
    context = {
        "blog_list": blog_list
    }
    return render(request, "blogs/blog_list.html", context)