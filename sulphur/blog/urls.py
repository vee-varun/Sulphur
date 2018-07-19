from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('posts/<int:offset>/<int:limit>/', views.posts, name='posts'),
    path('navs/', views.navs, name='navs'),
    path('foots/', views.foots, name='foots'),
    path('pages/', views.pages, name='pages'),
    path('categories/', views.categories, name='categories'),

    path('add_post/', views.add_new_post, name='add_post'),
    path('add_nav/', views.add_nav, name='add_nav'),
    path('add_foot/', views.add_foot, name='add_foot'),
    path('add_page/', views.add_page, name='add_page'),
    path('add_category/', views.add_category, name='add_category'),

    path('feed_new_post/', views.feed_new_post, name='feed_new_post'),
    path('feed_new_nav/', views.feed_new_nav, name='feed_new_nav'),
    path('feed_new_foot/', views.feed_new_foot, name='feed_new_foot'),
    path('feed_new_page/', views.feed_new_page, name='feed_new_page'),
    path('feed_new_category/', views.feed_new_category, name='feed_new_category'),

    path('single_post/<slug:cat>/<int:post_id>/<slug:post_title>/', views.single_post, name='single_post'),
    path('<slug:page_url>/', views.view_page, name='view_page'),
    path('<int:category_id>/<slug:category_url>/', views.category_page, name='category_page'),

    path('delete_post/<int:post_id>/', views.del_post, name='del_post'),
    path('delete_category/<int:category_id>/', views.del_category, name='del_category'),
    path('delete_page/<int:page_id>/', views.delete_page, name='delete_page'),
    path('delete_nav/<int:nav_id>/', views.delete_nav, name='delete_nav'),
    path('delete_foot/<int:foot_id>/', views.delete_foot, name='delete_foot'),

    path('edit_post/<slug:cat>/<int:post_id>/<slug:post_url>/', views.edit_post, name='edit_post'),
    path('edit_category/<int:category_id>/<slug:category_url>/', views.edit_category, name='edit_category'),
    path('edit_page/<int:page_id>/', views.edit_page, name='edit_page'),
    path('edit_nav/<int:nav_id>/', views.edit_nav, name='edit_nav'),
    path('edit_foot/<int:foot_id>/', views.edit_foot, name='edit_foot'),

    path('publish_post/<int:post_id>/', views.publish_post, name='publish_post'),
    path('publish_category/<int:category_id>/', views.publish_category, name='publish_category'),
    path('publish_page/<int:page_id>/', views.publish_page, name='publish_page'),
    path('publish_nav/<int:nav_id>/', views.publish_nav, name='publish_nav'),
    path('publish_foot/<int:foot_id>/', views.publish_foot, name='publish_foot'),

    path('unpublish/<int:post_id>/', views.unpublish_post, name='unpublish_post'),
    path('unpublish_category/<int:category_id>/', views.unpublish_category, name='unpublish_category'),
    path('unpublish_page/<int:page_id>/', views.unpublish_page, name='unpublish_page'),
    path('unpublish_nav/<int:nav_id>/', views.unpublish_nav, name='unpublish_nav'),
    path('unpublish_foot/<int:foot_id>/', views.unpublish_foot, name='unpublish_foot'),
]