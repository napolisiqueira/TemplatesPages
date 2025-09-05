from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    picture = models.ImageField(upload_to='about_pictures/')


    def __str__(self):
        return self.name
    

class Tag(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Galery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='galery_images/')
    tag = models.ManyToManyField(Tag, related_name='galeries', blank=True, default=None)


    def __str__(self):
        return self.title
    

class heroSection(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=300)
    background_image = models.ImageField(upload_to='hero_backgrounds/')

    class Meta:
        verbose_name = "Hero Section 1"
        verbose_name_plural = "Hero Sections 1"
    
    def __str__(self):
        return self.heading
    
class heroSection2(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=300)
    background_image = models.ImageField(upload_to='hero_backgrounds/')

    class Meta:
        verbose_name = "Hero Section 2"
        verbose_name_plural = "Hero Sections 2"


    def __str__(self):
        return self.heading
    
class heroSection3(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=300)
    background_image = models.ImageField(upload_to='hero_backgrounds/')

    class Meta:
        verbose_name = "Hero Section - Galery"
        verbose_name_plural = "Hero Sections - Galery"


    def __str__(self):
        return self.heading
    
class heroSection4(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=300)
    background_image = models.ImageField(upload_to='hero_backgrounds/')

    class Meta:
        verbose_name = "Hero Section - About"
        verbose_name_plural = "Hero Sections - About"


    def __str__(self):
        return self.heading


class Procediment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='procediment_images/')

    def __str__(self):
        return self.name
    

class AboutThings(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.title