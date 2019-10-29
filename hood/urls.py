from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('profile/', views.profile, name='profile'),
    path('post_business/', views.post_business, name='post_business'),
    path('search/', views.search_results, name='search'),
    path('notices/', views.notices, name='notices'),
    path('facilities/', views.facilities, name='facilities'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
