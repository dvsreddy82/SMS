
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Language(models.Model):
    language_Id = models.CharField(max_length=100)
    language_name = models.CharField(max_length=100)
    language_description = models.CharField(max_length=200)

    def __unicode__(self):
       return  self.language_Id + ' : ' + self.language_name

class Locale_String(models.Model):
    language = models.ForeignKey(Language)
    localestring_Id = models.CharField(max_length=100)
    localestring_value = models.CharField(max_length=300)
    last_updated_date= models.DateField(default=timezone.now)
    def __unicode__(self):
       return self.localestring_Id + ' : ' + self.localestring_value
    
class Locale_String_History(models.Model):
    localestring = models.ForeignKey(Locale_String)
    localestring_value = models.CharField(max_length=300)
    localestring_version = models.CharField(max_length=10)
    updated_date= models.DateField(default=timezone.now)
    def __unicode__(self):
       return  self.localestring + ' : ' + self.localestring_value
