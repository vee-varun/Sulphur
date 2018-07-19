from django.shortcuts import render, redirect
from sulphur.lib.fetcher import top_posts, all_navs, all_foots, all_pages, all_categories
from .forms import new_post_form, new_nav_form, new_foot_form, new_page_form, new_category_form, xedit_category_form, xedit_page_form, xedit_post_form
from django.utils import timezone
from sulphur.lib.authentication import is_loggedin
from django.template.defaultfilters import slugify
from .models import Post, Category
from sadmin.models import User


# ----------------- All Posts------------
#if the variable for pagination
def posts(request, offset, limit):
    if is_loggedin(request):
        record_list = top_posts(offset, limit)
        return render(request, 'blog/posts.html', {'record_list': record_list})
    else:
        msg = 'You`\re not logged in.'
        return render(request, 'debug.html', {'message': msg})
    
# It show the all nav links
def navs(request):
    if is_loggedin(request):
        nav_links = all_navs()
        return render(request, 'blog/navs.html', {'nav_links': nav_links})
    else:
        msg = 'You`\re not logged in.'
        return render(request, 'debug.html', {'message': msg})

# Show all the footer content
def foots(request):
    if is_loggedin(request):
        foot_list = all_foots()
        return render(request, 'blog/foots.html', {'foots': foot_list})
    else:
        msg = 'You`\re not logged in.'
        return render(request, 'debug.html', {'message': msg})

def pages(request):
    if is_loggedin(request):
        page_list = all_pages()
        return render(request, 'blog/pages.html', {'page_list': page_list})
    else:
        msg = 'You`\re not logged in.'
        return render(request, 'debug.html', {'message': msg})

def categories(request):
    if is_loggedin(request):
        category_list = all_categories()
        return render(request, 'blog/categories.html', {'category_list': category_list})
    else:
        msg = 'You`\re not logged in.'
        return render(request, 'debug.html', {'message': msg})


# ---------------- Add new post form---------
# It render the add new post form
def add_new_post(request):
    active = True
    if is_loggedin(request):
        return render(request, 'blog/new_post.html', {'active': active, 'new_post_form': new_post_form})
    else:
        active = False
        return render(request, 'blog/new_post.html', {'message': 'You can\'t add post, you are not logged in', 'active': active})

# It render the add new nav form
def add_nav(request):
    active = True
    if is_loggedin(request):
        return render(request, 'blog/new_nav.html', {'active': active, 'new_nav_form': new_nav_form})
    else:
        active = False
        return render(request, 'blog/new_nav.html', {'message': 'You can\'t add post, you are not logged in', 'active': active})

# It renders the add foot form  
def add_foot(request):
    active = True
    if is_loggedin(request):
        return render(request, 'blog/new_foot.html', {'active': active, 'new_foot_form': new_foot_form})
    else:
        active = False
        return render(request, 'blog/new_foot.html', {'message': 'You can\'t add post, you are not logged in', 'active': active})

# It render the add new page form
def add_page(request):
    active = True
    if is_loggedin(request):
        return render(request, 'blog/new_page.html', {'active': active, 'new_page_form': new_page_form})
    else:
        active = False
        return render(request, 'blog/new_post.html', {'message': 'You can\'t add post, you are not logged in', 'active': active})
    
def add_category(request):
    active= True
    if is_loggedin(request):
        return render(request, 'blog/new_category.html', {'active': active, 'new_category_form': new_category_form})
    else:
        active = False
        return render(request, 'blog/new_post.html', {'message': 'You can\'t add post, you are not logged in', 'active': active})

# --------------- Feeding into database------
# It add the new post data into database
def feed_new_post(request):

    if is_loggedin(request):
        if request.method == 'POST' or request.method == 'FILES':
            # Validating the form
            blog_post = new_post_form(request.POST, request.FILES)
            if blog_post.is_valid():
                #Extracting the data
                author = User.objects.get(login = request.session['username'])
                data = {
                    'title': blog_post.cleaned_data['title'],
                    'cover_pic': blog_post.cleaned_data['cover_pic'],
                    'content': blog_post.cleaned_data['content'],
                    'author': author,
                    'pub_date': timezone.now(),
                    'view_count': 0,
                    'url': slugify(blog_post.cleaned_data['title']),
                    'unlisted': 0,
                    'last_modified': timezone.now(),
                    'is_page': 0,
                    'in_nav': 0,
                    'in_footer': 0,
                    'keywords' : blog_post.cleaned_data['keywords'],
                    'description' : blog_post.cleaned_data['description'],
                    'social': 0,
                    'category': Category.objects.get(pk = blog_post.cleaned_data['category']),
                }
                # Instance of the Model Post
                n_p = Post(
                    title = data['title'],
                    cover_pic = data['cover_pic'],
                    content = data['content'],
                    author = data['author'],
                    pub_date = data['pub_date'],
                    view_count = data['view_count'],
                    url = data['url'],
                    unlisted = data['unlisted'],
                    last_modified = data['last_modified'],
                    is_page = data['is_page'],
                    in_nav = data['in_nav'],
                    in_footer = data['in_footer'],
                    keywords = data['keywords'],
                    description = data['description'],
                    social = data['social'],
                    category = data['category'],
                )
                n_p.save()
                return redirect('../posts/1/10/')
            else:
                msg = 'Form not cleaned. Page blog.views.py | Line 152'
                return render(request, 'debug.html', {'message': msg})
        else:
            msg = 'Invalid Access. Page blog.views.py | Line 26'
            return render(request, 'debug.html', {'message': msg})
    else:
        msg = 'Not logged in. Page blog.views.py | Line 29'
        return render(request, 'debug.html', {'message': msg})

# It will feed the new nav info into the database
def feed_new_nav(request):
    if is_loggedin(request):
        if request.method == 'POST':
            nav_form = new_nav_form(request.POST)
            if nav_form.is_valid():
                # Extracting Data
                author = User.objects.get(login=request.session['username'])
                data ={
                    'title': nav_form.cleaned_data['name'],
                    'content': '',
                    'author': author,
                    'pub_date': timezone.now(),
                    'view_count': 0,
                    'url': nav_form.cleaned_data['url'],
                    'unlisted': 0,
                    'last_modified': timezone.now(),
                    'is_page': 0,
                    'in_nav': 1,
                    'in_footer': 0,
                    'keywords': '',
                    'description': '',
                    'social': 0,
                }

                n_n = Post(
                    title = data['title'],
                    content = data['content'],
                    author = data['author'],
                    pub_date = data['pub_date'],
                    view_count = data['view_count'],
                    url = data['url'],
                    unlisted = data['unlisted'],
                    last_modified = data['last_modified'],
                    is_page = data['is_page'],
                    in_nav = data['in_nav'],
                    in_footer = data['in_footer'],
                    keywords = data['keywords'],
                    description = data['description'],
                    social = data['social'],
                )
                n_n.save()
                return redirect('../navs/')
            else:
                msg = 'Form not cleaned. Page blog.views.py | Line 175'
                return render(request, 'debug.html', {'message': msg})
        else:
            msg = 'Invalid Access. Page blog.views.py | Line 178'
            return render(request, 'debug.html', {'message': msg})
    else:
        msg = 'Not logged in. Page blog.views.py | Line 181'
        return render(request, 'debug.html', {'message': msg})

        
# Feed the footer data into database
def feed_new_foot(request):
    if is_loggedin(request):
        if request.method == 'POST':
            foot_form = new_foot_form(request.POST)
            if foot_form.is_valid():
                #Extracting Data
                author = User.objects.get(login=request.session['username'])
                data = {
                    'title': foot_form.cleaned_data['title'],
                    'content': foot_form.cleaned_data['content'],
                    'author': author,
                    'pub_date': timezone.now(),
                    'view_count': 0,
                    'url': foot_form.cleaned_data['url'],
                    'unlisted': 1,
                    'last_modified': timezone.now(),
                    'is_page': 0,
                    'in_nav': 0,
                    'in_footer': 1,
                    'keywords': '',
                    'description': '',
                    'social': 0,
                }
                n_f = Post(
                    title = data['title'],
                    content = data['content'],
                    author = data['author'],
                    pub_date = data['pub_date'],
                    view_count = data['view_count'],
                    url = data['url'],
                    unlisted = data['unlisted'],
                    last_modified = data['last_modified'],
                    is_page = data['is_page'],
                    in_nav = data['in_nav'],
                    in_footer = data['in_footer'],
                    keywords = data['keywords'],
                    description = data['description'],
                    social = data['social'],
                )
                n_f.save()
                return redirect('../foots/')
            else:
                msg = 'Form not cleaned. Page blog.views.py | Line 230'
                return render(request, 'debug.html', {'message': msg})
        else:
            msg = 'Invalid Access. Page blog.views.py | Line 233'
            return render(request, 'debug.html', {'message': msg})
    else:
        msg = 'Not logged in. Page blog.views.py | Line 236'
        return render(request, 'debug.html', {'message': msg})


# Add new static page into the database
def feed_new_page(request):
    if is_loggedin(request):
        if request.method == 'POST' or request.method == 'FILES':
            # Validating the form
            page_form = new_page_form(request.POST, request.FILES)
            if page_form.is_valid():
                # Extracting the data
                author = User.objects.get(login=request.session['username'])
                data = {
                    'title': page_form.cleaned_data['title'],
                    'cover_pic': page_form.cleaned_data['cover_pic'],
                    'content': page_form.cleaned_data['content'],
                    'author': author,
                    'pub_date': timezone.now(),
                    'view_count': 0,
                    'url': slugify(page_form.cleaned_data['title']),
                    'unlisted': 0,
                    'last_modified': timezone.now(),
                    'is_page': 1,
                    'in_nav': 0,
                    'in_footer': 0,
                    'keywords' : page_form.cleaned_data['keywords'],
                    'description' : page_form.cleaned_data['description'],
                    'social': 0,
                }
                # Instance of page
                n_p = Post(
                    title = data['title'],
                    cover_pic = data['cover_pic'],
                    content = data['content'],
                    author = data['author'],
                    pub_date = data['pub_date'],
                    view_count = data['view_count'],
                    url = data['url'],
                    unlisted = data['unlisted'],
                    last_modified = data['last_modified'],
                    is_page = data['is_page'],
                    in_nav = data['in_nav'],
                    in_footer = data['in_footer'],
                    keywords = data['keywords'],
                    description = data['description'],
                    social = data['social'],
                )
                n_p.save()
                return redirect('../pages/')
            else:
                msg = 'Form not cleaned. Page blog.views.py | Line 230'
                return render(request, 'debug.html', {'message': msg})
        else:
            msg = 'Invalid Access. Page blog.views.py | Line 233'
            return render(request, 'debug.html', {'message': msg})
    else:
        msg = 'Not logged in. Page blog.views.py | Line 236'
        return render(request, 'debug.html', {'message': msg})

# Adding new category into the database
def feed_new_category(request):
    if is_loggedin(request):
        if request.method == 'POST' or request.method == 'FILES':
            cat_form = new_category_form(request.POST, request.FILES)
            if cat_form.is_valid():
                data = {
                    'name': cat_form.cleaned_data['name'],
                    'cover_pic': cat_form.cleaned_data['cover_pic'],
                    'date_created': timezone.now(),
                    'url': slugify(cat_form.cleaned_data['name']),
                    'keywords': cat_form.cleaned_data['keywords'],
                    'description': cat_form.cleaned_data['description'],
                }
                n_c = Category(
                    name = data['name'],
                    cover_pic = data['cover_pic'],
                    date_created = data['date_created'],
                    url = data['url'],
                    keywords = data['keywords'],
                    description = data['description'],
                )
                n_c.save()
                return redirect('../categories/')
            else:
                msg = 'Form not cleaned. Page blog.views.py | Line 230'
                return render(request, 'debug.html', {'message': msg})
        else:
            msg = 'Invalid Access. Page blog.views.py | Line 233'
            return render(request, 'debug.html', {'message': msg})
    else:
        msg = 'Not logged in. Page blog.views.py | Line 236'
        return render(request, 'debug.html', {'message': msg})


# -------------- display-----------------
# It display the single post
def single_post(request,cat,post_id,post_title):
    single_post = Post.objects.get(pk = post_id)
    return render(request, 'blog/single_post.html', {'single_post': single_post})

# It display the single post
def view_page(request,page_url):
    page_obj = Post.objects.get(url=page_url)
    return render(request, 'blog/view_page.html', {'page_obj': page_obj})

def category_page(request, category_id, category_url):
    category_obj = Category.objects.get(pk=category_id)
    category_posts = Post.objects.filter(category=category_obj)
    return render(request, 'blog/category_page.html', {'category_obj': category_obj, 'category_posts': category_posts})



# -------- Delete post, page, nav, footer ----
def del_post(request, post_id):
    if is_loggedin(request):
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect('../../posts/1/10/')
    else:
        msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 379'
        return render(request, 'debug.html', {'message': msg})

def del_category(request, category_id):
    if is_loggedin(request):
        category = Category.objects.get(pk=category_id)
        category.delete()
        return redirect('../../categories/')
    else:
        msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 388'
        return render(request, 'debug.html', {'message': msg})

def delete_page(request, page_id):
    if is_loggedin(request):
        page = Post.objects.get(pk=page_id)
        page.delete()
        return redirect('../../pages/')
    else:
        msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 388'
        return render(request, 'debug.html', {'message': msg})

def delete_nav(request, nav_id):
    if is_loggedin(request):
        nav = Post.objects.get(pk=nav_id)
        nav.delete()
        return redirect('../../navs/')
    else:
        msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 388'
        return render(request, 'debug.html', {'message': msg})

def delete_foot(request, foot_id):
    if is_loggedin(request):
        foot = Post.objects.get(pk=foot_id)
        foot.delete()
        return redirect('../../foots/')
    else:
        msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 388'
        return render(request, 'debug.html', {'message': msg})

#---------Editing post, page, nav, footer -----
def edit_post(request, cat, post_id, post_url):
    if request.method == 'POST' or request.method == 'FILES':
        # Validating the form
        post = xedit_post_form(request.POST)
        if post.is_valid():
            #Extracting the data
            author = User.objects.get(login = request.session['username'])
            data = {
                'title': post.cleaned_data['title'],
                'content': post.cleaned_data['content'],
                'url': slugify(post.cleaned_data['title']),
                'last_modified': timezone.now(),
                'keywords' : post.cleaned_data['keywords'],
                'description' : post.cleaned_data['description'],
                'category': Category.objects.get(pk = post.cleaned_data['category']),
            }
            # Instance of the Model Post
            n_p = Post.objects.get(pk=post_id)
            n_p.title = data['title']
            n_p.content = data['content']
            n_p.url = data['url']
            n_p.last_modified = data['last_modified']
            n_p.keywords = data['keywords']
            n_p.description = data['description']
            n_p.category = data['category']
            n_p.save()
            return redirect('../../../../posts/1/10/')
        else:
            msg = 'Form not cleaned. Page blog.views.py | Line 230'
            return render(request, 'debug.html', {'message': msg})
    else:
        if is_loggedin(request):
            active = True
            post = Post.objects.get(pk=post_id)
            # Data to be filled in the editing post form
            data_dict = {
                'title': post.title,
                'content': post.content,
                'keywords': post.keywords,
                'description': post.description,
                'category': post.category
            }
            # Filling up the data into the edit form
            edit_post_form = new_post_form(data_dict)
            return render(request, 'blog/edit_post.html', {'active': active, 'post': post, 'edit_post_form': edit_post_form})
        else:
            msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 379'
            return render(request, 'debug.html', {'message': msg})

def edit_category(request, category_id, category_url):
    if request.method == 'POST' or request.method == 'FILES':
        # Validating the form
        category = xedit_category_form(request.POST)
        if category.is_valid():
            #Extracting the data
            author = User.objects.get(login = request.session['username'])
            data = {
                'name': category.cleaned_data['name'],
                'last_modified': timezone.now(),
                'url': slugify(category.cleaned_data['name']),
                'keywords' : category.cleaned_data['keywords'],
                'description' : category.cleaned_data['description'],

            }
            # Instance of the Model Post
            n_c = Category.objects.get(pk=category_id)
            n_c.name = data['name']
            n_c.last_modified = data['last_modified']
            n_c.keywords = data['keywords']
            n_c.url = data['url']
            n_c.description = data['description']
            n_c.save()
            return redirect('../../../categories/')
    else:
        if is_loggedin(request):
            active = True
            category = Category.objects.get(pk=category_id)
            # Data to be filled in the editing post form
            data_dict = {
                'name': category.name,
                'keywords': category.keywords,
                'description': category.description,
            }
            # Filling up the data into the edit form
            edit_category_form = new_category_form(data_dict)
            return render(request, 'blog/edit_category.html', {'active': active, 'category': category, 'edit_category_form': edit_category_form})
        else:
            msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 379'
            return render(request, 'debug.html', {'message': msg})
        
def edit_page(request, page_id):
    if request.method == 'POST' or request.method == 'FILES':
        # Validating the form
        page_incoming_form = xedit_page_form(request.POST)
        if page_incoming_form.is_valid():
            # Etracting the data
            author = User.objects.get(login = request.session['username'])
            data = {
                'title': page_incoming_form.cleaned_data['title'],
                'content': page_incoming_form.cleaned_data['content'],
                'keywords': page_incoming_form.cleaned_data['keywords'],
                'description': page_incoming_form.cleaned_data['description'],
                'last_modified': timezone.now(),
                'url': slugify(page_incoming_form.cleaned_data['title']),
            }
            n_p = Post.objects.get(pk=page_id)
            n_p.title = data['title']
            n_p.content = data['content']
            n_p.keywords = data['keywords']
            n_p.descriptipn = data['description']
            n_p.last_modified = data['last_modified']
            n_p.url = data['url']
            n_p.save()
            return redirect('../../pages/')
    else:
        if is_loggedin(request):
            active = True
            page = Post.objects.get(pk=page_id)
            # Data to be filled into the form
            data_dict = {
                'title': page.title,
                'content': page.content,
                'keywords': page.keywords,
                'description': page.description,
            }
            # Filling up the data into the edit form
            edit_page_form = new_page_form(data_dict)
            return render(request, 'blog/edit_page.html', {'active': active, 'page': page, 'edit_page_form': edit_page_form})

def edit_nav(request, nav_id):
    if request.method == 'POST' or request.method == 'FILES':
        # Validating the form
        nav_incoming_form = new_nav_form(request.POST)
        if nav_incoming_form.is_valid():
            # Etracting the data
            author = User.objects.get(login = request.session['username'])
            data = {
                'title': nav_incoming_form.cleaned_data['name'],
                'last_modified': timezone.now(),
                'url': nav_incoming_form.cleaned_data['url'],
            }
            n_n = Post.objects.get(pk=nav_id)
            n_n.title = data['title']
            n_n.last_modified = data['last_modified']
            n_n.url = data['url']
            n_n.save()
            return redirect('../../navs/')
    else:
        if is_loggedin(request):
            active = True
            nav = Post.objects.get(pk=nav_id)
            # Data to be filled into the form
            data_dict = {
                'name': nav.title,
                'url': nav.url,
            }
            # Filling up the data into the edit form
            edit_nav_form = new_nav_form(data_dict)
            return render(request, 'blog/edit_nav.html', {'active': active, 'nav': nav, 'edit_nav_form': edit_nav_form})

def edit_foot(request, foot_id):
    if request.method == 'POST' or request.method == 'FILES':
        # Validating the form
        foot_incoming_form = new_foot_form(request.POST)
        if foot_incoming_form.is_valid():
            # Etracting the data
            author = User.objects.get(login = request.session['username'])
            data = {
                'title': foot_incoming_form.cleaned_data['title'],
                'last_modified': timezone.now(),
                'content': foot_incoming_form.cleaned_data['content'],
                'url': foot_incoming_form.cleaned_data['url'],
            }
            n_f = Post.objects.get(pk=foot_id)
            n_f.title = data['title']
            n_f.content = data['content']
            n_f.last_modified = data['last_modified']
            n_f.url = data['url']
            n_f.save()
            return redirect('../../foots/')
    else:
        if is_loggedin(request):
            active = True
            foot = Post.objects.get(pk=foot_id)
            # Data to be filled into the form
            data_dict = {
                'title': foot.title,
                'content': foot.content,
                'url': foot.url,
            }
            # Filling up the data into the edit form
            edit_foot_form = new_foot_form(data_dict)
            return render(request, 'blog/edit_foot.html', {'active': active, 'foot': foot, 'edit_foot_form': edit_foot_form})



#------------ Publish post, category, page, nav, foot-----
def publish_post(request, post_id):
    if is_loggedin(request):
        post = Post.objects.get(pk=post_id)
        post.unlisted = 0
        post.save()
        return redirect('../../posts/1/10/')
    else:
        msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 439'
        return render(request, 'debug.html', {'message': msg})

def publish_category(request, category_id):
    if is_loggedin(request):
        category = Category.objects.get(pk=category_id)
        category.unlisted = 0
        category.save()
        return redirect('../../categories/')
    else:
        msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 449'
        return render(request, 'debug.html', {'message': msg})

def publish_page(request, page_id):
    if is_loggedin(request):
        page = Post.objects.get(pk=page_id)
        page.unlisted = 0
        page.save()
        return redirect('../../pages/')
    else:
        msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 449'
        return render(request, 'debug.html', {'message': msg})

def publish_nav(request, nav_id):
    if is_loggedin(request):
        nav = Post.objects.get(pk=nav_id)
        nav.unlisted = 0
        nav.save()
        return redirect('../../navs/')
    else:
        msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 449'
        return render(request, 'debug.html', {'message': msg})

def publish_foot(request, foot_id):
    if is_loggedin(request):
        foot = Post.objects.get(pk=foot_id)
        foot.unlisted = 0
        foot.save()
        return redirect('../../foots/')
    else:
        msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 449'
        return render(request, 'debug.html', {'message': msg})


# ------------ Unpublish post, category, page, nav, footer
def unpublish_post(request, post_id):
    if is_loggedin(request):
        post = Post.objects.get(pk=post_id)
        post.unlisted = 1
        post.save()
        return redirect('../../posts/1/10/')
    else:
        msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 451'
        return render(request, 'debug.html', {'message': msg})

def unpublish_category(request, category_id):
    if is_loggedin(request):
        category = Category.objects.get(pk=category_id)
        category.unlisted = 1
        category.save()
        return redirect('../../categories/')
    else:
        msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 461'
        return render(request, 'debug.html', {'message': msg})

def unpublish_page(request, page_id):
    if is_loggedin(request):
        page = Post.objects.get(pk=page_id)
        page.unlisted = 1
        page.save()
        return redirect('../../pages/')
    else:
        msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 449'
        return render(request, 'debug.html', {'message': msg})

def unpublish_nav(request, nav_id):
    if is_loggedin(request):
        nav = Post.objects.get(pk=nav_id)
        nav.unlisted = 1
        nav.save()
        return redirect('../../navs/')
    else:
        msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 449'
        return render(request, 'debug.html', {'message': msg})

def unpublish_foot(request, foot_id):
    if is_loggedin(request):
        foot = Post.objects.get(pk=foot_id)
        foot.unlisted = 1
        foot.save()
        return redirect('../../foots/')
    else:
        msg = 'Access Denied for non-admin user. Page: Blog.views.py Line: 449'
        return render(request, 'debug.html', {'message': msg})