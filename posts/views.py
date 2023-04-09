#django
from django.shortcuts import render
#Utilities
from datetime import datetime

#Data posts
posts = [
    {
        'name': 'Robert John Linder',
        'username': 'Johnny Silverhand',
        'age': '27',
        'timestamp': datetime.now().strftime('%A %d de %B de %Y. Hora: %H:%M:%S%p'),
        'profilePicture': 'https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/styles/hc_1440x810/public/media/image/2021/12/cyberpunk-2077-johnny-silverhand-keanu-reeves-2567861.jpg?itok=1zhR0CFK',
        'imgPost': 'https://cloudfront-us-east-1.images.arcpublishing.com/infobae/3MSH4NDQ6BFDXBQ3BLURL354DI.jpg',
    },
    {
        'name': 'V',
        'username': 'cazoni',
        'age': '25',
        'timestamp': datetime.now().strftime('%A %d de %B de %Y. Hora: %H:%M:%S%p'),
        'profilePicture': 'https://alfabetajuega.com/hero/2020/07/Cyberpunk-2077.jpg?width=1200&aspect_ratio=16:9',
        'imgPost': 'https://i.blogs.es/024bf8/cyberpunk2077_lucky_number_13_rgb-en/1366_2000.jpeg',
    },
    {
        'name': 'Kirito',
        'username': 'El espadachin puerco',
        'age': '17',
        'timestamp': datetime.now().strftime('%A %d de %B de %Y. Hora: %H:%M:%S%p'),
        'profilePicture': 'https://static.wikia.nocookie.net/sao/images/5/56/Doble_empuñadura_Kirito.png/revision/latest?cb=20130107144520&path-prefix=es',
        'imgPost': 'https://i.ytimg.com/vi/GwGd3teG6gg/maxresdefault.jpg',
    }
]
# Create your views here.

def post(request):
    return render(request, 'feed.html', {'posts': posts})