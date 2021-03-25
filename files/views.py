from django.shortcuts import render
from services.file_saver_service import FileSavingService
from .forms import UploadFileForm


def upload(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = request.FILES['file']
            print(uploaded_file.name, uploaded_file.content_type)

            saving_service = FileSavingService()
            url = saving_service.save(uploaded_file)

            return render(request, 'file_upload_form.html', {'url': url})
    else:
        form = UploadFileForm()
    return render(request, 'file_upload_form.html', {'form': form})



