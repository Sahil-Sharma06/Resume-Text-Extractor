from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage
from .utils import extract_text_from_pdf
from .llms_utils import get_structured_resume 
def home(request):
    return HttpResponse("<h1>Welcome to Resume Extractor API</h1><p>Go to <a href='/api/upload/'>API Upload</a></p>")

@api_view(["POST"])
def upload_resume(request):
    if "resume" not in request.FILES:
        return Response({"error": "No file uploaded"}, status=400)

    file = request.FILES["resume"]
    file_path = default_storage.save(f"resumes/{file.name}", file)

    extracted_text = extract_text_from_pdf(default_storage.path(file_path))
    structured_data = get_structured_resume(extracted_text)  # Use LLaMA API

    return Response({"structured_resume": structured_data})