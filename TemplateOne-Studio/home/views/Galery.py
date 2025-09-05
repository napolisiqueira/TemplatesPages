from django.shortcuts import render
from home.models import Galery, heroSection3

def galery(request):
    hero_Section3 = heroSection3.objects.get()
    gallery1 = Galery.objects.filter(tag__nome='Estudio')
    gallery2 = Galery.objects.filter(tag__nome='Equipamentos')
    gallery3 = Galery.objects.filter(tag__nome='Fotos')

    context = {
        'gallery1': gallery1,
        'gallery2': gallery2,
        'gallery3': gallery3,
        'hero_Section3': hero_Section3,
    }

    return render(request, 'galery.html', context)