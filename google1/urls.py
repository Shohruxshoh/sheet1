from django.urls import path
from . import views

urlpatterns = [
    path('auth/google/', views.google_auth, name='google_auth'),
    path('auth/google/callback/', views.google_auth_callback, name='google_auth_callback'),
    # Qolgan URL-lar
]
