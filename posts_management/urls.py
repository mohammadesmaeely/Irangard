from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path
from posts_management.views import PostView

urlpatterns = [
    path('post/', PostView.as_view()),
]
