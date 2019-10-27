""" GameArtist URL Configuration """

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gameartist.apps.landing.urls')),
    path('blog/', include('gameartist.apps.blog.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('', include('gameartist.apps.accounts.urls')),
    path('', include('django.contrib.auth.urls')),
    path('cookies/', include('gameartist.apps.cookie_policy.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
