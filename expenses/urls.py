from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('', views.dashboard, name='dashboard'),          # /
    path('dashboard/', views.dashboard, name='dashboard'),# /dashboard/
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('update/<int:expense_id>/', views.update_expense, name='update_expense'),
]
