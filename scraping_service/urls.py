from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('scrap/', include('scraping.urls')),
    path('crud/', include('crud.urls')),
    path('zvk/', include('zvk.urls')),
    path('pcus/', include('pcus.urls')),
    path('boss_says/', include('boss_says.urls')),
    path('cara/', include('cara.urls', namespace='cara')),
    path('ck/', include('ck11.urls', namespace='ck11')),
    path('srdk/', include('srdk.urls', namespace='srdk')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
