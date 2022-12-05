from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('recruiter_dashboard', views.recruiter_dashboard_view, name='recruiter_dashboard'),
    path('posts/create', views.posts_create_view),
    path('posts/update/<int:id>', views.posts_update_view, name='posts_update_view'),
]
