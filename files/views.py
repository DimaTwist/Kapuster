from django.shortcuts import render
from services.file_saver_service import FileSavingService
# from django.core.files.storage import FileSystemStorage


def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        saving = FileSavingService()
        url = saving.save(uploaded_file.name, uploaded_file)

        return render(request, 'file_upload_form.html', {'url': url})
    else:
        return render(request, 'file_upload_form.html')

