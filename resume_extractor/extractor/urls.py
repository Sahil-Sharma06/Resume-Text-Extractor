from django.urls import path
from .views import upload_resume, home  # Import views

urlpatterns = [
    path("", home, name="home"),  # Homepage
    path("upload/", upload_resume, name="upload_resume"),  # Upload endpoint
]
