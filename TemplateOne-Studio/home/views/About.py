from django.shortcuts import render
from home.models import About, heroSection4, AboutThings

def about(request):
    hero_Section4 = heroSection4.objects.get()
    about = About.objects.get()
    things = AboutThings.objects.all()  

    context = {
        'hero_Section4': hero_Section4,
        'about': about,
        'things': things,
    }

    return render(request, 'about.html', context)