from django.shortcuts import render
from home.models import About_Us, Hero_Section4

def about(request):
    hero_section4 = Hero_Section4.objects.get()
    about_us = About_Us.objects.get()

    context = {
        'Hero_Section4': hero_section4,
        'About_Us': about_us,
    }

    return render(request, 'about.html', context)