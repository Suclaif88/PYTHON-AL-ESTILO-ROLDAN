from django.http import HttpResponse

def Saludo(request): #vista
    
    return HttpResponse("HOLA MI PAPACHO")