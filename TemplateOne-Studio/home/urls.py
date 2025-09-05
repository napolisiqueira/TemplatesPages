from django.urls import path
from . import views


app_name="home"

urlpatterns = [
    path('', views.home, name='home'),
    path('galery', views.galery, name='galery'),
    path('about', views.about, name='about'),
    path('procediments', views.procediments, name='procediments'),
]
