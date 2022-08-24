from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model): 
    name = models.CharField(max_length=50)
    capital = models.CharField(max_length=50,blank=True, null=True)
    region = models.CharField(max_length=50, blank=True,null=True)
    subregion = models.CharField(max_length=50,blank=True,null=True)
    population = models.PositiveBigIntegerField(default=0)
    languages = models.JSONField(blank=True, null=True, default=list)
    currencies = models.JSONField(blank=True,null=True, default=list)
    image = models.URLField(blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ["name"]
    
    
