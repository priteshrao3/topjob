from django.db import models

# Create your models here.
class Slider(models.Model):
    image = models.ImageField(upload_to="sliderimg")
    title = models.CharField(max_length=150)
    Content = models.TextField( max_length=2000)


class ServicePage(models.Model):
    Service_Title =models.CharField(max_length=50)
    First_Service_Image = models.ImageField(upload_to="servimg1" )
    First_Service_Content = models.TextField( max_length=2000)
    Service_Subtitle = models.CharField(max_length=200)
    Second_Service_Content = models.TextField( max_length=2000)
    Second_Service_Image = models.ImageField(upload_to="servimg2" )
    
    
    def title_to_url(self):
        return self.Service_Title.replace(' ', '-')
    


class Project(models.Model):
    image = models.ImageField(upload_to="projectimg" )
    Project_name = models.CharField( max_length=100)



class Testomonial(models.Model):
    image = models.ImageField(upload_to="testmoimg" )
    clint_coments = models.TextField( max_length=1000)
    name = models.CharField( max_length=100)
    designation = models.TextField( max_length=100)



