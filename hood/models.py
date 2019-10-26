from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hood(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    image = models.ImageField(upload_to='hood_photo', blank=True, default='hood_photo/hood.jpg')
    occupants = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_photo', blank=True, default='profile_photo/defaultprofile.jpg')
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, default='myHood')
    bio = models.CharField(max_length=255, blank=True)
    contacts = models.CharField(max_length=200)

    def __str__(self):
        return self.hood


class Business(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    image = models.ImageField(upload_to='biz_pic/', blank=True, default='biz_pic/bizpic.jpg')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, default='no business')
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, default='myHood')
