from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    population = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    police = models.CharField(max_length=250,null=True)
    health = models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.name
    @classmethod
    def find_neighborhood(cls,name):
        return cls.objects.filter(name__icontains=name).all
class UserProfile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/',default='SOME IMAGE')
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="userprofile")
    contact = models.IntegerField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    id_number = models.IntegerField(blank=True,null=True)
    hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,related_name="hood",blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    
    def save_userprofile(self):
        self.save()
    def delete_userprofile(self):
        self.delete() 
    
    @receiver(post_save, sender=User)
    def save_user(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

class Business(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="business")
    hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    email = models.EmailField()
    def __str__(self):
        return self.name
    def save_business(self):
        self.save()
    def delete_business(self):
        self.delete()
    
    def update_business():
        pass
    @classmethod
    def find_business(cls,name):
        return cls.objects.filter(name__icontains=name).all


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    post = models.CharField(max_length=6000)

    def save_post(self):
        self.save()
    def delete_post(self):
        self.delete()
    
    def __str__(self):
        return self.post