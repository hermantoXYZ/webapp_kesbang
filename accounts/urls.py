# accounts/urls.py

from django.urls import path
from . import views, viewsAdmin, viewsStaff, viewsPelanggan
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView, CustomPasswordResetConfirmView

urlpatterns = [
    path('', views.signup_view, name='home'),
    # Accounts 
    path('login/', views.login_view, name='login'),
    path('accounts/login/', views.login_view, name='profile'),
    path('register/', views.signup_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    #Reset Password

    path('accounts/password/reset/', CustomPasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('accounts/reset/password/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('accounts/password/reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    #Admin
    path('dashboard/admin/', viewsAdmin.admin, name='dashboard_admin'),
    #Staff
    path('dashboard/staff/', viewsStaff.staff, name='dashboard_staff'),
    path('dashboard/staff/list/', viewsStaff.list_pengajuan, name='list_pengajuan'),
    path('staff/view/<uuid:register_id>/', viewsStaff.view_pengajuan, name='view_pengajuan'),
    #Pelanggan/PenerimaManfaat
    path('dashboard/', viewsPelanggan.pelanggan, name='dashboard_pelanggan'),
    path('dashboard/profile/', viewsPelanggan.dashboard_profile, name='profile'),
    path('dashboard/profile/staff', viewsStaff.dashboard_profile_staff, name='profile_staff'),
    
    path('dashboard/profile/update/', viewsPelanggan.update_profile, name='update_profile'),


]