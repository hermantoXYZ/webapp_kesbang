# modelform/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/pemohon', views.pemohon, name='pemohon'),
    path('dashboard/create/', views.create_register, name='create_register'),
    path('dashboard/list/', views.register_list, name='register_list'),
    path('dashboard/terverifikasi/', views.dashboard_terverifikasi, name='dashboard_terverifikasi'),
    path('dashboard/unverified/', views.dashboard_unverified, name='dashboard_unverified'),
    path('pemohon/edit/<uuid:register_id>/', views.edit_pemohon, name='edit_pemohon'),
    path('organisasi/edit/<uuid:register_id>/', views.edit_organisasi, name='edit_organisasi'),
    path('pengurus/edit/<uuid:register_id>/', views.edit_pengurus, name='edit_pengurus'),
    path('dokumen/edit/<uuid:register_id>/', views.edit_dokumen, name='edit_dokumen'),
    path('resume/<uuid:register_id>/', views.resume_page, name='resume_page'),
    path('akhiri-pendaftaran/<uuid:register_id>/', views.akhiri_pendaftaran, name='akhiri_pendaftaran'),
    # Tambahkan pola URL lainnya sesuai aplikasi Anda
]
