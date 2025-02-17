from django.urls import path
from .views import upload_resume # Import views

urlpatterns = [
    path("upload/", upload_resume, name="upload_resume"),  # Upload endpoint
]
