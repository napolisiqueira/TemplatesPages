# settings_app/admin.py

from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import SiteSettings, NavbarLink, FooterText, FooterSocialLink

# Classes Inline para os modelos relacionados
class NavbarLinkInline(admin.TabularInline):
    """
    Inline admin para o modelo NavbarLink.
    """
    model = NavbarLink
    extra = 1
    fields = ['name', 'url', 'order', 'is_external']
    sortable_field_name = 'order'

class FooterTextInline(admin.TabularInline):
    """
    Inline admin para o modelo FooterText.
    """
    model = FooterText
    extra = 1
    fields = ['title', 'content', 'order']
    sortable_field_name = 'order'

class FooterSocialLinkInline(admin.TabularInline):
    """
    Inline admin para o modelo FooterSocialLink.
    """
    model = FooterSocialLink
    extra = 1
    fields = ['platform', 'url', 'order']
    sortable_field_name = 'order'

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    """
    Admin para o modelo SiteSettings.
    Gerencia as configurações globais do site e os inlines de navegação e rodapé.
    """
    inlines = [NavbarLinkInline, FooterTextInline, FooterSocialLinkInline]

    fieldsets = (
        ('Configurações Gerais', {
            'fields': (
                'navbar_title',
                'site_name_home',
                'site_name_about',
                'site_name_galery',
                'favicon',
                'whatsapp_link',
            )
        }),
        ('Controle de Exibição das Seções', {
            'fields': (
                ('show_navbar', 'show_footer'),
                ('show_hero_section_1', 'show_hero_section_2', 'show_hero_section_3', 'show_hero_section_4'),
                ('show_make_section', 'show_procediments_section'),
                ('show_about_section', 'show_about_section_2'),
                ('show_galery_section', 'show_galery_procediments_section'),
            )
        }),
    )

    list_display = ('site_name_home', 'show_navbar', 'show_footer')
    list_display_links = ('site_name_home',)

    def has_add_permission(self, request):
        """
        Impede a criação de mais de uma instância do modelo SiteSettings.
        """
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """
        Impede a exclusão do objeto de configurações, garantindo que sempre exista um.
        """
        return False

    def save_model(self, request, obj, form, change):
        """
        Sobrescreve o método save_model para garantir que apenas uma instância exista,
        mesmo se o usuário tentar criar uma via outra rota.
        """
        if not change and SiteSettings.objects.exists():
            raise ValidationError('Já existe uma instância de SiteSettings. Altere a existente.')
        super().save_model(request, obj, form, change)