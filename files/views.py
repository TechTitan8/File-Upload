from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import FileUploadForm
from .models import UploadedFile

@login_required
def home(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            UploadedFile.objects.create(
                user=request.user,
                filename=file.name,
                content_type=file.content_type,
                file_data=file.read()
            )
            return redirect('home')
    else:
        form = FileUploadForm()
    
    files = UploadedFile.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'home.html', {'form': form, 'files': files})

@login_required
def download_file(request, file_id):
    file = UploadedFile.objects.get(id=file_id, user=request.user)
    response = HttpResponse(file.file_data, content_type=file.content_type)
    response['Content-Disposition'] = f'attachment; filename="{file.filename}"'
    return response
