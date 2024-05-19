from django.urls import path
from .views import inicio, agregar_producto, cerrar_sesion
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', inicio, name='inicio'),
    path('agregar/', agregar_producto, name='agregar_producto'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', cerrar_sesion, name='logout'),
]