from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage
from .utils import extract_structured_resume

@api_view(["POST"])
def upload_resume(request):
    if "resume" not in request.FILES:
        return Response({"error": "No file uploaded"}, status=400)

    file = request.FILES["resume"]
    file_path = default_storage.save(f"resumes/{file.name}", file)

    structured_data = extract_structured_resume(default_storage.path(file_path))

    return Response({"structured_resume": structured_data})
