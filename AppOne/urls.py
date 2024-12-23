from django.urls import path
from .views import ApponeView



urlpatterns = [
    path('appone/', ApponeView.as_view(), name="appone"),
    path('appone/<int:id>/', ApponeView.as_view(), name="id_put/patch"),
    
    ]