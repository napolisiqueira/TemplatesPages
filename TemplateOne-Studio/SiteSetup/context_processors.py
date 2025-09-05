# settings_app/context_processors.py

from .models import SiteSettings

def site_settings(request):
    try:
        settings = SiteSettings.objects.get()
        navbar_links = settings.navbar_links.all()
        footer_texts = settings.footer_texts.all()
        footer_social_links = settings.footer_social_links.all()
        


    except SiteSettings.DoesNotExist:
        # Retorna um dicionário vazio para evitar erros
        return {}

    return {
        'site_settings': settings,
        'navbar_links': navbar_links,
        'footer_texts': footer_texts,
        'footer_social_links': footer_social_links,
    }