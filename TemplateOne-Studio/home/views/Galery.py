from django.shortcuts import render
from home.models import GalleryImage, Hero_Section3

def galery(request):
    hero_section3 = Hero_Section3.objects.get()
    gallery1 = GalleryImage.objects.filter(tag__name='estudio')
    gallery2 = GalleryImage.objects.filter(tag__name='equipamentos')
    gallery3 = GalleryImage.objects.filter(tag__name='fotos')

    context = {
        'gallery1': gallery1,
        'gallery2': gallery2,
        'gallery3': gallery3,
        'Hero_Section3': hero_section3,
    }

    return render(request, 'galery.html', context)