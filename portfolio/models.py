from django.db import models
from django.urls import reverse

class DesignerDetails(models.Model):
    name = models.CharField(max_length=50)
    prof_pic = models.ImageField()
    personaldescription = models.TextField(max_length=500)
    education = models.CharField(max_length= 50)
    school = models.CharField(max_length=50)
    schooldescription = models.TextField(max_length=50)
    schoolstiestamp = models.DateTimeField(auto_now_add= True)
    skills = models.CharField(max_length= 50)
    skillscapacity = models.IntegerField() #I want to show ability in percentage mode
    job = models.CharField(max_length= 50)
    company = models.CharField(max_length=50)
    workingtime = models.DateTimeField(auto_now_add= True)
    jobsdescription = models.TextField(max_length=50)

    def __str__(self):
        return self.name

class ArtCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __str__(self):
        return reverse('category', kwarg={'id':self.id})

class Art(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField()
    size = models.IntegerField()
    description = models.TextField(max_length= 500)
    datemade = models.DateTimeField(auto_now_add= True)
    categorie = models.ForeignKey(ArtCategory, on_delete=models.CASCADE)
    featured = models.BooleanField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('art-details', kwarg= {'id':self.id})

class Hires(models.Model):
    name = models.CharField(max_length= 50)
    subject = models.CharField(max_length= 50)
    senderemail = models.EmailField()
    message = models.TextField()
    time_choosen = models.TimeField()
    time = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hired', kwarg={'id':self.id})