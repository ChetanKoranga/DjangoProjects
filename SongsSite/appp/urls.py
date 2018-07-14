from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views

app_name='appp'

urlpatterns = [
    #appp
path('', views.pen, name='pen'),
    # /718/
re_path(r'(?P<album_id>[0-9]+)/', views.detail, name='detail'),

re_path(r'(?P<album_id>[0-9]+)/favorite', views.favorite, name='favorite'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
\