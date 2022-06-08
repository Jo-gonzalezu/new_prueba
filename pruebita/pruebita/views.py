from django.http import HttpResponse
from django.template import Template, Context 

def inicio(request):
    doc_externo = open("static/index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()         #ejecuta python
    documento = plt.render(ctx)
    return HttpResponse(documento)      #devuelve html

