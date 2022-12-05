from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('recruiter_dashboard', views.recruiter_dashboard_view, name='recruiter_dashboard'),
    path('candidate_dashboard', views.candidate_dashboard_view, name='candidate_dashboard'),

    path('posts/', views.posts_all_view, name='posts_all_view'),
    path('posts/create', views.posts_create_view),
    path('posts/update/<int:id>', views.posts_update_view, name='posts_update_view'),
    path('posts/delete/<int:id>', views.posts_delete_view, name='posts_delete_view'),
    path('posts/<int:id>', views.posts_view, name='posts_view'),
    path('posts/interest/<int:id>', views.posts_interest_view, name='posts_interest'),

    path('offers/create/<int:id>', views.offer_create_view, name='offer_create'),
    path('offers/<int:id>', views.offer_view, name='offer_view'),
    path('offers/respond/<int:id>', views.offer_respond_view, name='offer_respond')
]
