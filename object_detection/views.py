from django.shortcuts import render, redirect
from .forms import ImageFeedForm
from .models import ImageFeed
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Убедитесь, что у вас есть шаблон home.html
@login_required
def dashboard(request):
    images = ImageFeed.objects.filter(user=request.user)
    return render(request, 'object_detection/dashboard.html', {'images': images})

@login_required
def add_image_feed(request):
    if request.method == 'POST':
        form = ImageFeedForm(request.POST, request.FILES)
        if form.is_valid():
            image_feed = form.save(commit=False)
            image_feed.user = request.user
            image_feed.save()
            # Здесь можно добавить вызов функции для обработки изображения
            return redirect('dashboard')
    else:
        form = ImageFeedForm()
    return render(request, 'object_detection/add_image_feed.html', {'form': form})