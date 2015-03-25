from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return self.user.username

class Industry(models.Model):
    industry = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.industry

class StartUp(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000)
    creator = models.ForeignKey('UserProfile')
    industry = models.ForeignKey('Industry')
    likes = models.IntegerField()
    
    def __unicode__(self):
        return self.name

class Keywords(models.Model):
    keyword = models.CharField(max_length=32)
    startUp = models.ForeignKey('StartUp')
    
    def __unicode__(self):
        return self.keyword + " - " + self.startUp
# Create your models here.
