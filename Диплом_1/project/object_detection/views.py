# object_detection/views.py

from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import ImageFeed

def home(request):
    return render(request, 'object_detection/home.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_feed = ImageFeed(image=form.cleaned_data['image'])
            image_feed.save()
            # Здесь можно добавить код для обработки изображения, если необходимо
            return redirect('dashboard')
    else:
        form = ImageUploadForm()
    return render(request, 'object_detection/add_image_feed.html', {'form': form})

def dashboard(request):
    images = ImageFeed.objects.all()
    return render(request, 'object_detection/dashboard.html', {'images': images})

def login_view(request):
    # Логика для входа пользователя
    return render(request, 'object_detection/login.html')

def register(request):
    # Логика для регистрации пользователя
    return render(request, 'object_detection/register.html')