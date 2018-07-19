from django.urls import path
from . import views

app_name = 'themes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>/<slug:category_name>/', views.cat, name='cat'),
    path('<slug:category_name>/<int:post_id>/<slug:post_title>/', views.post, name='post'),
]