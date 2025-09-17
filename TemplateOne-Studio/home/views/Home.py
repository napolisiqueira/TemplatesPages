from django.shortcuts import render
from home.models import Hero_Section1, Hero_Section2, What_We_Do, About_Us, GalleryImage, Procediments

def home(request):
    hero_Section1 = Hero_Section1.objects.get()
    hero_Section2 = Hero_Section2.objects.get()
    what_we_do_section = What_We_Do.objects.get()
    about_us = About_Us.objects.get()
    gallery_images = GalleryImage.objects.all()[:6]
    procediments = Procediments.objects.all()

    context = {
        'Hero_Section1': hero_Section1,
        'Hero_Section2': hero_Section2,
        'What_We_Do': what_we_do_section,
        'About_Us': about_us,
        'GalleryImage': gallery_images,
        'Procediments': procediments,
    }

    return render(request, 'home.html', context)