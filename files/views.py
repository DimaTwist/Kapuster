from django.shortcuts import render
from services.file_saver_service import FileSavingService, BlobStorage
# from django.core.files.storage import FileSystemStorage
from django.core.files import uploadedfile
import os


def upload(request):
    if request.method == "POST":
        uploaded_file = uploadedfile.UploadedFile(request.FILES['document']) # InMemory object
        storage = BlobStorage()
        saving = FileSavingService(uploaded_file, storage)
        url = saving.save()

        return render(request, 'file_upload_form.html', {'url': url})
    else:
        return render(request, 'file_upload_form.html')

