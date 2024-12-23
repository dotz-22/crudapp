from django.urls import path
from .views import ApptwoView



urlpatterns = [
    path('apptwo/', ApptwoView.as_view(), name="apptwo"),
    path('apptwo/<int:id>/', ApptwoView.as_view(), name="id_put/patch2"),
    
    ]