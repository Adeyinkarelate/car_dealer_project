from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team_image/%Y/%m/%d')
    facebook_link = models.URLField(max_length=255,blank=True)
    twitter_link = models.URLField(max_length=255 ,blank=True)
    goole_plus_link = models.URLField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
