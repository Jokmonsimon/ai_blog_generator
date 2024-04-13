from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('create-account', views.user_create_account, name='create-account'),
    path('logout', views.user_logout, name='logout'),
    path('generate-blog', views.generate_blog, name='generate-blog')
]