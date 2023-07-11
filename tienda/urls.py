from django.conf import settings
from django.conf.urls.static import static

# Resto de tus URLs...

urlpatterns = [
    # ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




from django.urls import path

from tienda import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('buscar/', views.buscar, name='buscar'),
]
