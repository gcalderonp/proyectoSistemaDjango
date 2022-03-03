from unicodedata import name
from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', inicio, name='inicio'),
    path('nosotros', nosotros, name='nosotros'),
    path('libros', libros, name='libros'),
    path('libros/crear', create, name='crear'),
    path('libros/editar', edit, name='editar'),
    path('libros/eliminar/<int:id>', delete, name='eliminar'),
    path('libros/editar/<int:id>', edit, name='editar'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)