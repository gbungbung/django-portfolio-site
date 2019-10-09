from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prof_pic = models.ImageField(upload_to='user_directory_path')
    bio = models.TextField(max_length=500)
    hobbies = models.TextField()
    phone_number = models.CharField(max_length= 50)

#Create storage folder for instance user
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user_id, filename)

#Signals the builtin User model if there is change in Model 
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Resume(models.Model):
    title = models.CharField(max_length= 50)
    organisation = models.CharField(max_length= 50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    #categorie = models.ManyToManyField(CvCategory)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resumedetail', kwargs={'pk':self.pk})

class Art(models.Model):
    title = models.CharField(max_length=50)
    #designer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='webmedia/%Y/%m/%d/')
    description = models.TextField(max_length= 500)
    datemade = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('artdetail', kwargs={'pk':self.pk})

class Hires(models.Model):
    name = models.CharField(max_length= 50)
    Your_email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hires', kwargs={'pk':self.pk})