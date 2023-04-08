#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime

def hello_world(request):
    """Variable que guarda la hora actual"""
    now = datetime.now().strftime('%A %d de %B de %Y. Hora: %H:%M:%S%p')
    """Return a greeting"""
    return HttpResponse('Oa, estas es la hora local del servidor xD {now}'.format(now=str(now)))

def sortJson(request):
    import json
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sortedNumbers = sorted(numbers)
    #Variable diccionario de datos
    data = {
        'status': 'ok',
        'numbers': sortedNumbers,
        'message': 'Todo salio bien!'
    }
    #Se utiliza en content_type='application/json' para decirle a la pagina que se enviara un formato json y el indent=3
    #es para añadir saltos de parrafo 
    return HttpResponse(json.dumps(data, indent=3), content_type='application/json')

def hi(request, name, age):
    if age < 18:
        message = 'Lo siento {}, sos cachorro'.format(name)
    else: 
        message = 'Bienvenido pajerin {}'.format(name)
    return HttpResponse(message)
