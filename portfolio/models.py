from django.db import models
from datetime import datetime

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=600)
    image = models.ImageField(upload_to = 'images/')
    body = models.TextField()
    Category = models.CharField(max_length=100, blank=True)
    languages = models.CharField(max_length=200, blank=True)
    date = models.DateField(blank=True, null=True)
    url = models.CharField(max_length=200, blank=True)
    homepage = models.ImageField(upload_to = 'images/', blank=True)
    screenshot1 = models.ImageField(upload_to = 'images/', blank=True)
    screenshot2 = models.ImageField(upload_to = 'images/', blank=True)

    def __str__(self):
        return self.title

class Myskill(models.Model):
    title = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.title

class Contact(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  subject = models.CharField(max_length=200)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.name
