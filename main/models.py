from distutils.command.upload import upload
from django.db import models
from django.urls import reverse

# Create your models here.
class All_Mult(models.Model): 
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to = 'static/img')
    URL = models.SlugField(unique=True, null=True)
    description = models.TextField()
    season_num = models.IntegerField()
    release_date = models.DateField()
    rating = models.IntegerField()

    def get_absolute_url(self): 
        return reverse('Season_url',kwargs={'slug':self.URL})

    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name_plural = "Мультики"
        verbose_name = 'Мультик'


class All_Season(models.Model): 
    mult = models.ForeignKey(All_Mult,on_delete=models.CASCADE,null=True)
    season_num = models.IntegerField()
    photo = models.ImageField(upload_to = 'static/img')
    description = models.TextField()
    release_date = models.DateField()

    def get_absolute_url(self): 
            return reverse('Series_url',kwargs={'slug':self.mult.URL,'season_num':self.season_num})

    def __str__(self):
        return str(self.season_num) + ' сезон - ' + str(self.mult)
    
    class Meta: 
        verbose_name_plural = "Сезоны"
        verbose_name = 'Сезон'


class All_Series(models.Model):
    series_num = models.IntegerField( null=True)
    season = models.ForeignKey(All_Season,on_delete=models.CASCADE,null=True)
    link = models.CharField(max_length=100)
    def __str__(self):
        return "1 серия " + str(self.season)
    
    class Meta: 
        verbose_name_plural = "Серии"
        verbose_name = 'Серия'


class Long_Mult(models.Model):
    mult = models.ForeignKey(All_Mult,on_delete=models.CASCADE,null=True)
    link = models.CharField(max_length=100)
    def __str__(self):
        return "Длинный мультик "  + str(self.mult)
    class Meta: 
        verbose_name_plural = "Длинные мультики"
        verbose_name = 'Мультик'



# class Comment(models.Model): 
#     series = models.ForeignKey(All_Series)