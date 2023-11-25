from django.contrib import admin
from core.models import Slider, ServicePage, Project, Testomonial
    

# Register your models here.
# @admin.register(Slider)
# class CarouselAdmin(admin.ModelAdmin):
#     list_display = ('id', 'image', 'title')

@admin.register(ServicePage)
class ServicePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'Service_Title', 'First_Service_Content', 'First_Service_Image', 'Service_Subtitle', 'Second_Service_Content', 'Second_Service_Image')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'Project_name')


@admin.register(Testomonial)
class TestomonialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'clint_coments', 'name', 'designation')
