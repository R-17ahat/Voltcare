
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('register/', views.register, name='register'),

    path('login/', views.customer_login, name='login'),

    path('dashboard/', views.customer_dashboard, name='dashboard'),

    path('submit-complaint/', views.submit_complaint, name='submit_complaint'),

    path('track-complaint/', views.track_complaint, name='track_complaint'),

    path('complaint-history/', views.complaint_history, name='complaint_history'),

    path('logout/', views.customer_logout, name='logout'),
]
