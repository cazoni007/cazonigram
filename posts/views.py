#django
from django.shortcuts import render
from django.http import HttpResponse
#Utilities
from datetime import datetime

#Data posts
posts = [
    {
        'name': 'Robert John Linder',
        'username': 'Johnny Silverhand',
        'age': '27',
        'timestamp': datetime.now().strftime('%A %d de %B de %Y. Hora: %H:%M:%S%p'),
        'img': 'https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/styles/hc_1440x810/public/media/image/2021/12/cyberpunk-2077-johnny-silverhand-keanu-reeves-2567861.jpg?itok=1zhR0CFK'
    },
    {
        'name': 'V',
        'username': 'cazoni',
        'age': '25',
        'timestamp': datetime.now().strftime('%A %d de %B de %Y. Hora: %H:%M:%S%p'),
        'img': 'https://alfabetajuega.com/hero/2020/07/Cyberpunk-2077.jpg?width=1200&aspect_ratio=16:9'
    },
    {
        'name': 'Kirito',
        'username': 'El espadachin puerco',
        'age': '17',
        'timestamp': datetime.now().strftime('%A %d de %B de %Y. Hora: %H:%M:%S%p'),
        'img': 'https://static.wikia.nocookie.net/sao/images/5/56/Doble_empuñadura_Kirito.png/revision/latest?cb=20130107144520&path-prefix=es'
    }
]
# Create your views here.

def post(request):
    """Creamos una lista que almacenara los posts"""
    contenido = []
    """Un For el cual añadira la lista de posts que creamos arriba a la lista de contenido, y ademas el tipo de letra. Con html"""
    for post in posts:
        contenido.append("""
            <p><strong>{name} - <i>{username}</i></strong></p>
            <p><small>{age} - <i>{timestamp}</i></small></p>
            <figure><img src="{img}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(contenido))