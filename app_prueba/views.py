from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def inicio(request):
    return render(request, 'inicio.html')


@login_required
def agregar_producto(request):
    if request.method == 'POST':
        # Lógica para agregar el producto aquí
        return redirect('inicio')  # Redirigir a la página de inicio después de agregar el producto
    else:
        return render(request, 'agregar_producto.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')