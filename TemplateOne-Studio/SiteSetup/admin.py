# settings_app/admin.py

from django.contrib import admin
from .models import SiteSettings, NavbarLink, FooterText, FooterSocialLink

# Classes Inline para os modelos relacionados
class NavbarLinkInline(admin.TabularInline):
    model = NavbarLink
    extra = 1
    fields = ['name', 'url', 'order', 'is_external']
    sortable_field_name = 'order'

class FooterTextInline(admin.TabularInline):
    model = FooterText
    extra = 1
    fields = ['title', 'content', 'order']
    sortable_field_name = 'order'

class FooterSocialLinkInline(admin.TabularInline):
    model = FooterSocialLink
    extra = 1
    fields = ['platform', 'url', 'order']
    sortable_field_name = 'order'


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    # Adiciona os inlines para permitir a edição dos links e textos
    inlines = [NavbarLinkInline, FooterTextInline, FooterSocialLinkInline]

    # Organiza os campos em grupos para melhor visualização
    fieldsets = (
        ('Configurações Gerais', {
            'fields': ('site_name_home', 'site_name_about', 'site_name_galery', 'favicon', 'whatsapp_link')
        }),
        ('Controle de Exibição das Seções', {
            'fields': ('show_navbar', 'show_hero_section_1', 'show_about_section', 'show_galery_section', 'show_hero_section_2', 'show_footer')
        }),
        ('Conteúdo da Navbar e Título', {
            'fields': ('navbar_title',)
        }),
    )

    # Impede a criação de mais de uma instância do modelo
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    # Impede a exclusão do objeto de configurações
    def has_delete_permission(self, request, obj=None):
        return False

    # Personaliza a exibição na lista do admin
    list_display = ('site_name_home', 'show_navbar', 'show_footer')
    list_display_links = ('site_name_home',)