from django.http import HttpResponse
from django.template import Template, Context

def Saludo(request): #vista
    
    nombre = "Sebas"
    
    doc_externo=open("C:/Users/sebaq/OneDrive/Escritorio/ESCRITORIO/PYTHON-AL-ESTILO-ROLDAN/Django/PR1/Plantillas/plantilla1.html")
    
    plt = Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx = Context({"nombre_persona":nombre})
    
    documento = plt.render(ctx)
    
    return HttpResponse(documento)
