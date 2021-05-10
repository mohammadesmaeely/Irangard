from django.urls import path
from . import views, ticket_views

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('register/', views.Register.as_view()),
    path('ticket/', ticket_views.TicketView.as_view()),
    path('state/', views.StateView.as_view())
]
