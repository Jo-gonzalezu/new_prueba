from django.http import HttpResponse
from django.template import Template, Context 

def inicio(request):
    doc_externo = open("static/index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)      

def seguimiento(request):
    doc_externo = open("views\seguir.html") 
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)     

def registro(request):
    doc_externo = open("static\views\register_new.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)         

def fundacion(request):
    doc_externo = open("static\views\donaciones.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)         

def productos(request):
    doc_externo = open("static\views\productos.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)         