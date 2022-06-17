from django.http import HttpResponse
from django.template import Template, Context 
from django.shortcuts import render 
from productos.models import Productos

def login(request):
    return render(request,"views_html/register_new.html")

# para acceder a los parametros get se debe utilizar la siguiente sintaxis
def resultado(request):
    #mensaje = f'se ha logeado el usuario {request.GET["correo"]}'
    llamadabd = Productos.objects.filter(nombre_icontains="plantita_weed")
    return render(request,"static/views_html/resulado.html",{'mensaje':mensaje})

def inicio(request):
    doc_externo = open("static/index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)      

def seguimiento(request):
    doc_externo = open("static/views_html/seguir.html") 
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)     

def registro(request):
    doc_externo = open("static/views_html/register_new.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)         

def fundacion(request):
    doc_externo = open("static/views_html/donaciones.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)         

def productos(request):
    doc_externo = open("static/views_html/productos.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)         