from django.shortcuts import render
from blog.models import Post, Category
from sadmin.models import User
from sulphur.forms import signupform

# Create your views here.
def index(request):
    users = User.objects.all()
    if len(users) < 1:
        return render(request, 'config.html', {'signupform': signupform})
    else:   
        page = Post.objects.all()
        categories = Category.objects.filter(unlisted=0)
        return render(request, 'sulphate/index.html', {'page': page, 'categories': categories})

def cat(request, category_id, category_name):
    get_category = Category.objects.get(pk=category_id)
    posts = Post.objects.filter(category=get_category).filter(unlisted=0)
    return render(request, 'sulphate/category.html', {'posts': posts, 'category': get_category})

def post(request, category_name, post_id, post_title):
    post = Post.objects.get(pk=post_id)
    return render(request, 'sulphate/post.html', {'post': post})
