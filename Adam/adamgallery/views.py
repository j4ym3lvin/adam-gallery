from django.shortcuts import render


def home (request):
    return render(request, 'home.html')

def album_view(request):
    return render(request, 'adamgallery/album.html')

def images_folder(request):
    # Logic to display images
    return render(request, 'images.html')  # Create an 'images.html' template

def videos_folder(request):
    # Logic to display videos
    return render(request, 'videos.html')  # Create a 'videos.html' template
