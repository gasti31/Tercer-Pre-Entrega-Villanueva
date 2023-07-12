from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
#from . import views
from tienda import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('buscar/', views.buscar, name='buscar'),
    path('inicio-sesion/', auth_views.LoginView.as_view(template_name='sign-up.html'), name='inicio-sesion'),
    path('cerrar-sesion/', auth_views.LogoutView.as_view(), name='cerrar-sesion'),
    path('agregar-producto/', views.agregar_producto, name='agregar-producto'),
    path('buscar-producto/', views.buscar_producto, name='buscar-producto'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

