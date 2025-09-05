from django.shortcuts import render
from home.models import About, Galery, heroSection, heroSection2, Procediment

def procediments(request):
    hero_Section1 = heroSection.objects.get()
    procediments = Procediment.objects.all()

    context = {
        'hero_Section1': hero_Section1,
        'procediments': procediments,
    }

    return render(request, 'procediments.html', context)