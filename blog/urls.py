from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name="allblogs" ),
    path('<int:blog_id>/', views.detail, name='detail'), #? look for an integer after /blog and it will look for the unique id
] 
