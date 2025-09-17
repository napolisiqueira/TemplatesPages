from django.db import models

class Hero_Section1(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=300)
    background_image = models.ImageField(upload_to='hero_backgrounds/')

    class Meta:
        verbose_name = "Hero Section 1 - Home"
        verbose_name_plural = "Hero Sections 1 - Home"
    
    def __str__(self):
        return self.heading
    
class Hero_Section2(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=300)
    background_image = models.ImageField(upload_to='hero_backgrounds/')

    class Meta:
        verbose_name = "Hero Section 2 - Home"
        verbose_name_plural = "Hero Sections 2 - Home"


    def __str__(self):
        return self.heading
    
class Hero_Section3(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=300)
    background_image = models.ImageField(upload_to='hero_backgrounds/')

    class Meta:
        verbose_name = "Hero Section - Galeria"
        verbose_name_plural = "Hero Sections - Galeria"


    def __str__(self):
        return self.heading
    
class Hero_Section4(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=300)
    background_image = models.ImageField(upload_to='hero_backgrounds/')

    class Meta:
        verbose_name = "Hero Section - Sobre Nós"
        verbose_name_plural = "Hero Sections - Sobre Nós"


    def __str__(self):
        return self.heading

class Hero_Section5(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=300)
    background_image = models.ImageField(upload_to='hero_backgrounds/')

    class Meta:
        verbose_name = "Hero Section - Procedimentos"
        verbose_name_plural = "Hero Sections - Procedimentos"


    def __str__(self):
        return self.heading


class What_We_Do(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='what_we_do_icons/')

    class Meta:
        verbose_name = "Seção 'O Que Fazemos'"
        verbose_name_plural = "Seção 'O Que Fazemos'"

    def __str__(self):
        return self.title
    

class Procediments(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='procediment_images/')

    class Meta:
        verbose_name = "Seção 'Procedimento'"
        verbose_name_plural = " Seção 'Procedimentos'"

    def __str__(self):
        return self.title
    
class About_Us(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='about_pictures/')

    class Meta:
        verbose_name = "Seção 'Sobre Nós'"
        verbose_name_plural = "Seção 'Sobre Nós'"

    def __str__(self):
        return self.name
    


class Metrics(models.Model):
    # This field creates the link between a metric and an About Us page.
    about_us_page = models.ForeignKey(
        About_Us,
        on_delete=models.CASCADE,
        related_name='metrics_cards',
        verbose_name='Página Sobre Nós'
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)

    class Meta:
        verbose_name = "Métrica"
        verbose_name_plural = "Métricas"

    def __str__(self):
        return self.title
    
class GalleryTag(models.Model):
    TAG_CHOICES = [
        ('estudio', 'Estúdio'),
        ('equipamentos', 'Equipamentos'),
        ('fotos', 'Fotos'),
    ]
    name = models.CharField(max_length=50, choices=TAG_CHOICES, unique=True, verbose_name='Nome da Tag')

    class Meta:
        verbose_name = 'Tag da Galeria'
        verbose_name_plural = 'Tags da Galeria'

    def __str__(self):
        return self.get_name_display()


class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Título (opcional)')
    image = models.ImageField(upload_to='gallery/', verbose_name='Imagem')
    tag = models.ForeignKey(
        GalleryTag,
        on_delete=models.PROTECT,
        related_name='images',
        verbose_name='Tag'
    )

    class Meta:
        verbose_name = 'Imagem da Galeria'
        verbose_name_plural = 'Imagens da Galeria'

    def __str__(self):
        return f'{self.title or "Sem Título"} ({self.tag.get_name_display()})'