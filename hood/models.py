from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hood(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    image = models.ImageField(upload_to='hood_photo', blank=True, default='hood_photo/hood.jpg')
    occupants = models.PositiveSmallIntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_photo', blank=True, default='profile_photo/defaultprofile.jpg')
    bio = models.CharField(max_length=255, blank=True)
    contacts = models.CharField(max_length=200)
    join_date = models.DateTimeField(auto_now_add=True)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, default='myHood')

    def __str__(self):
        return f'{self.user.username}'


class Business(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='biz_pic/', blank=True, default='biz_pic/bizpic.jpg')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, default='no business')
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, default='myHood')

    def __str__(self):
        return f'{self.name}'
