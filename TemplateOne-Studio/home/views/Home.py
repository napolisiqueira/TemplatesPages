from django.shortcuts import render
from home.models import About, Galery, heroSection, heroSection2, Procediment

def home(request):
    hero_Section1 = heroSection.objects.get()
    hero_Section2 = heroSection2.objects.get()
    galery = Galery.objects.all()[:6]
    procediments = Procediment.objects.all()

    context = {
        'hero_Section1': hero_Section1,
        'hero_Section2': hero_Section2,
        'galery': galery,
        'procediments': procediments,
    }

    return render(request, 'home.html', context)