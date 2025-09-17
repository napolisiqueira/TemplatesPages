# seu_app/admin.py

from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import (
    Hero_Section1, Hero_Section2, Hero_Section3, Hero_Section4, Hero_Section5,
    What_We_Do, Procediments, About_Us, Metrics, GalleryTag, GalleryImage
)

class MetricsInline(admin.TabularInline):
    model = Metrics
    extra = 1
    max_num = 5
    fields = ['title', 'description']


@admin.register(Hero_Section1)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'subheading')
    fieldsets = (
        (None, {'fields': ('heading', 'subheading', 'background_image')}),
    )

    def has_add_permission(self, request):
        return not Hero_Section1.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Hero_Section2)
class HeroSection2Admin(admin.ModelAdmin):
    list_display = ('heading', 'subheading')
    fieldsets = (
        (None, {'fields': ('heading', 'subheading', 'background_image')}),
    )

    def has_add_permission(self, request):
        return not Hero_Section2.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Hero_Section3)
class HeroSection3Admin(admin.ModelAdmin):
    list_display = ('heading', 'subheading')
    fieldsets = (
        (None, {'fields': ('heading', 'subheading', 'background_image')}),
    )

    def has_add_permission(self, request):
        return not Hero_Section3.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
        
@admin.register(Hero_Section4)
class HeroSection4Admin(admin.ModelAdmin):
    list_display = ('heading', 'subheading')
    fieldsets = (
        (None, {'fields': ('heading', 'subheading', 'background_image')}),
    )

    def has_add_permission(self, request):
        return not Hero_Section4.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Hero_Section5)
class HeroSection5Admin(admin.ModelAdmin):
    list_display = ('heading', 'subheading')
    fieldsets = (
        (None, {'fields': ('heading', 'subheading', 'background_image')}),
    )

    def has_add_permission(self, request):
        return not Hero_Section5.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(What_We_Do)
class WhatWeDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

    def has_add_permission(self, request):
        return not About_Us.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Procediments)
class ProcedimentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'image')
    list_filter = ('price',)
    search_fields = ('title',)

    def get_form(self, request, obj=None, **kwargs):
        if obj and obj.name:
            self.form.base_fields['title'].initial = obj.name
        return super().get_form(request, obj, **kwargs)

@admin.register(About_Us)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [MetricsInline] 
    list_display = ('name', 'image')

    def has_add_permission(self, request):
        return not About_Us.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(GalleryTag)
class GalleryTagAdmin(admin.ModelAdmin):
    """Admin para as tags da galeria."""
    list_display = ('name',)
    
    def has_add_permission(self, request):
        return GalleryTag.objects.count() < len(GalleryTag.TAG_CHOICES)

    def has_delete_permission(self, request, obj=None):
        return True

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    """Admin para as imagens da galeria."""
    list_display = ('title', 'tag')
    list_filter = ('tag',)
    search_fields = ('title',)