from django.shortcuts import render
from home.models import About_Us, GalleryImage, Hero_Section5, Procediments

def procediments(request):
    hero_section5 = Hero_Section5.objects.get()
    procediments = Procediments.objects.all()

    context = {
        'Hero_Section5': hero_section5,
        'Procediments': procediments,
    }

    return render(request, 'procediments.html', context)