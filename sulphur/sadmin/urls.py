from . import views
from django.urls import path

app_name = 'sadmin'
urlpatterns = [
    path('', views.sadmin, name='sadmin'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
]