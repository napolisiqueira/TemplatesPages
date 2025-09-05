from django.db import models
from django.core.exceptions import ValidationError

class SiteSettings(models.Model):
    # Campos de Título da Página
    site_name_home = models.CharField(max_length=100, default='Lash Design')
    site_name_about = models.CharField(max_length=100, default='Lash Design - Sobre')
    site_name_galery = models.CharField(max_length=100, default='Lash Design - Galeria')
    favicon = models.ImageField(upload_to='site/', blank=True, null=True, verbose_name='Favicon')
    whatsapp_link = models.URLField(max_length=200, blank=True, help_text='Ex: https://wa.me/seunumerodetelefone')

    show_navbar = models.BooleanField(default=True, verbose_name='Exibir Barra de Navegação')
    show_hero_section_1 = models.BooleanField(default=True, verbose_name='Exibir Seção "Hero 1"')
    show_about_section = models.BooleanField(default=True, verbose_name='Exibir Seção "Sobre"')
    show_galery_section = models.BooleanField(default=True, verbose_name='Exibir Seção "Galeria"')
    show_hero_section_2 = models.BooleanField(default=True, verbose_name='Exibir Seção "Hero 2"')
    show_procediments_section = models.BooleanField(default=True, verbose_name='Exibir Seção "Procedimentos"')
    show_footer = models.BooleanField(default=True, verbose_name='Exibir Rodapé')


    navbar_title = models.CharField(max_length=50, default='Lash Design')
    
    class Meta:
        verbose_name = 'Configurações do Site'
        verbose_name_plural = 'Configurações do Site'

    def save(self, *args, **kwargs):
        if SiteSettings.objects.exists() and not self.pk:
            raise ValidationError('Já existe uma instância de SiteSettings. Altere a existente.')
        return super(SiteSettings, self).save(*args, **kwargs)

    def __str__(self):
        return "Configurações Globais do Site"

class NavbarLink(models.Model):
    settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE, related_name='navbar_links')
    name = models.CharField(max_length=50, verbose_name='Nome do Link')
    url = models.CharField(max_length=200, verbose_name='URL do Link')
    order = models.IntegerField(default=0, verbose_name='Ordem de exibição')
    is_external = models.BooleanField(default=False, verbose_name='Link Externo', help_text='Marque se o link for externo ao site.')

    class Meta:
        ordering = ['order']
        verbose_name = 'Link da Navbar'
        verbose_name_plural = 'Links da Navbar'

    def __str__(self):
        return self.name

class FooterText(models.Model):
    settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE, related_name='footer_texts')
    title = models.CharField(max_length=50, verbose_name='Título')
    content = models.TextField(verbose_name='Conteúdo', help_text='Use HTML simples para formatação se necessário.')
    order = models.IntegerField(default=0, verbose_name='Ordem de exibição')

    class Meta:
        ordering = ['order']
        verbose_name = 'Conteúdo do Rodapé'
        verbose_name_plural = 'Conteúdos do Rodapé'
        
    def __str__(self):
        return self.title

class FooterSocialLink(models.Model):
    settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE, related_name='footer_social_links')
    platform = models.CharField(max_length=50, verbose_name='Plataforma (Ex: Instagram, Facebook)')
    url = models.URLField(max_length=200, verbose_name='URL')
    order = models.IntegerField(default=0, verbose_name='Ordem de exibição')

    class Meta:
        ordering = ['order']
        verbose_name = 'Link Social do Rodapé'
        verbose_name_plural = 'Links Sociais do Rodapé'

    def __str__(self):
        return self.platform