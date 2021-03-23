from django.shortcuts import render
from services.file_saver_service import FileSavingService, BlobStorage
# from django.core.files.storage import FileSystemStorage
from django.core.files import uploadedfile

from .forms import UploadFileForm
import os


def upload(request):

    if request.method == 'POST':

        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = request.FILES['file']
            print(uploaded_file.file)

            # storage = BlobStorage()
            # saving = FileSavingService(uploaded_file, storage)
            # url = saving.save()

            url = 'URL'
            return render(request, 'file_upload_form.html', {'url': url})
    else:
        form = UploadFileForm()
    return render(request, 'file_upload_form.html', {'form': form})



