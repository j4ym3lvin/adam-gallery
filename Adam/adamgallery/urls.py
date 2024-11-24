from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('album/', views.album_view, name='album'),
    path('images/', views.images_folder, name='images_folder'),  # Images folder
    path('videos/', views.videos_folder, name='videos_folder'),  # Videos folder
]