from django.contrib import admin
from .models import About, Galery, heroSection, heroSection2, heroSection3, heroSection4, Procediment, AboutThings, Tag

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    # Organiza os campos na tela de edição
    fieldsets = (
        ('Sobre a Pessoa', {'fields': ('name', 'content', 'picture')}),
    )
    # Exibe os campos na lista de objetos
    list_display = ('name',)

    # Limita o modelo a uma única instância (singleton)
    def has_add_permission(self, request):
        return About.objects.count() == 0

@admin.register(Galery)
class GaleryAdmin(admin.ModelAdmin):
    # Exibe os campos na lista de objetos
    list_display = ('title', 'image')

    # Limita a galeria a no máximo 50 fotos
    def has_add_permission(self, request):
        return Galery.objects.count() < 50

@admin.register(heroSection)
class heroSectionAdmin(admin.ModelAdmin):
    # Organiza os campos na tela de edição
    fieldsets = (
        ('Primeira Seção Hero', {'fields': ('heading', 'subheading', 'background_image')}),
    )
    # Exibe os campos na lista de objetos
    list_display = ('heading',)
    
    # Limita o modelo a uma única instância
    def has_add_permission(self, request):
        return heroSection.objects.count() == 0

@admin.register(heroSection2)
class heroSection2Admin(admin.ModelAdmin):
    # Organiza os campos na tela de edição
    fieldsets = (
        ('Segunda Seção Hero', {'fields': ('heading', 'subheading', 'background_image')}),
    )
    # Exibe os campos na lista de objetos
    list_display = ('heading',)

    # Limita o modelo a uma única instância
    def has_add_permission(self, request):
        return heroSection2.objects.count() == 0
    
@admin.register(heroSection3)
class heroSection3Admin(admin.ModelAdmin):
    # Organiza os campos na tela de edição
    fieldsets = (
        ('Seção Hero - Galeria', {'fields': ('heading', 'subheading', 'background_image')}),
    )
    # Exibe os campos na lista de objetos
    list_display = ('heading',)

    # Limita o modelo a uma única instância
    def has_add_permission(self, request):
        return heroSection3.objects.count() == 0
    

@admin.register(heroSection4)
class heroSection4Admin(admin.ModelAdmin):
    # Organiza os campos na tela de edição
    fieldsets = (
        ('Seção Hero - Sobre Nós', {'fields': ('heading', 'subheading', 'background_image')}),
    )
    # Exibe os campos na lista de objetos
    list_display = ('heading',)

    # Limita o modelo a uma única instância
    def has_add_permission(self, request):
        return heroSection4.objects.count() == 0

    
@admin.register(Procediment)
class ProcedimentAdmin(admin.ModelAdmin):
    # Organiza os campos na tela de edição
    fieldsets = (
        ('Procedimento', {'fields': ('name', 'price', 'description', 'image')}),
    )
    # Exibe os campos na lista de objetos
    list_display = ('name',)
    
    # Limita o modelo a no máximo 10 procedimentos
    def has_add_permission(self, request):
        return Procediment.objects.count() < 10

@admin.register(AboutThings)
class AboutThingsAdmin(admin.ModelAdmin):
    # Organiza os campos na tela de edição
    fieldsets = (
        ('Coisas Sobre Nós', {'fields': ('title', 'description')}),
    )
    # Exibe os campos na lista de objetos
    list_display = ('title',)
    
    # Limita o modelo a no máximo 10 itens
    def has_add_permission(self, request):
        return AboutThings.objects.count() < 5
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # Organiza os campos na tela de edição
    fieldsets = (
        ('Tag', {'fields': ('nome',)}),
    )
    # Exibe os campos na lista de objetos
    list_display = ('nome',)
    
    # Limita o modelo a no máximo 20 tags
    def has_add_permission(self, request):
        return Tag.objects.count() < 3