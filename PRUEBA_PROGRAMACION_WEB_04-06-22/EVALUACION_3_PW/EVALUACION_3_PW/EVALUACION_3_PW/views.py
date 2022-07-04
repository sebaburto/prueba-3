from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import redirect, render
from numpy import delete
from base_de_datos.models import Productos, ProductosAgregados, usuario

def inicio (request):
    return render(request,"index.html")

def login (request):
    return render(request,"login.html")
    
def carritodecompras (request):
    var_producto = ProductosAgregados.objects.all()
    contexto = {'fun_var_producto' :  var_producto}
    return render(request,'carritodecompras.html/',contexto)

def contacto (request):
    return render(request,"contacto.html")

def formulario (request):
    mensaje = "usuario creado"
    try:
        if request.method == "POST":
            usuario.objects.create(
                nombre_usuario = request.POST.get('usuariologeo'),
                contrasena = request.POST.get('password')
        )
        mensaje="usuario creado"
    except:
        mensaje = f'Los datos ingresados son inválidos, por favor intente nuevamente'

    contexto = {'mensaje':mensaje}
    return render(request,"formulario.html",contexto)



def agregarUsuario(request):
    return render(request, 'formulario.html')


def productos (request):
    return render(request,"productos.html")
    
def seguimiento (request):
    return render(request,"seguimiento.html")



def eliminarProducto(request,id):
    var_eliminar_producto = ProductosAgregados.objects.get(id=id)
    var_eliminar_producto.delete()
    return redirect('/carritodecompras/')

def agregarProducto(request):
    ProductosAgregados.objects.create(        
        nombre = "Ficus Benjamina",
        descripcion = "lorem",
        precio_normal = 6000,
        precio_usuario_registrado = 4800
    )
    return redirect('/carritodecompras/')

def agregarProducto2(request):
    ProductosAgregados.objects.create(        
        nombre = "Lavanda",
        descripcion = "lorem",
        precio_normal = 2500,
        precio_usuario_registrado = 2000
    )
    return redirect('/carritodecompras/')

def agregarProducto3(request):
    ProductosAgregados.objects.create(        
        nombre = "Hypoestes sanguinolenta",
        descripcion = "lorem",
        precio_normal = 3000,
        precio_usuario_registrado = 2400
    )
    return redirect('/carritodecompras/')



