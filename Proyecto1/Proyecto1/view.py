from django.http import HttpResponse
import  datetime
from django.template import Context, Template, loader


def saludar(request):
    return HttpResponse("Hola mundo!")

def segunda_vista(resquest):
    return HttpResponse("Ya entendi! esto es muy simple")

def dia_de_hoy(request):

    dia=datetime.datetime.today()
    cadena="Hoy es"+str(dia)
    return HttpResponse(cadena)

def saludo_con_nombre(self,nombre):
    return HttpResponse("<h1>Hola mi nombre es: "+nombre+"</h1>")

def calcular_edad_anios(self,edad):
    return HttpResponse("<h1>Tu año de nacimiento es: "+str(int(datetime.datetime.now().year)-int(edad))+"</h1>")

def probandoHtml(self):
   

    nom="Joaquin"
    ape="Fernandez"
    lista_de_notas=[9,5,3,2,6,6]

    diccionario={'nombre':nom , 'apellido':ape, 'lista': lista_de_notas}

    plantilla=loader.get_template('template1.html')


    documento=plantilla.render(diccionario)

    return HttpResponse(documento)



