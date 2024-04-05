from django.urls import path
from .views import FileWritingView
urlpatterns = [
    path('', FileWritingView.as_view()),
]
