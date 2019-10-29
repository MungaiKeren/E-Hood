from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hood(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    image = models.ImageField(upload_to='hood_photo', blank=True, default='hood_photo/hood.jpg')
    pub_date = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Facilities(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    contact = models.CharField(max_length=30)
    image = models.ImageField(upload_to='facilities', blank=True, default='facilities/sample.jpg')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_photo', blank=True, default='profile_photo/defaultprofile.jpg')
    bio = models.CharField(max_length=255, blank=True)
    contacts = models.CharField(max_length=200)
    join_date = models.DateTimeField(auto_now_add=True)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Business(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='biz_pic/', blank=True, default='biz_pic/bizpic.jpg')
    details = models.TextField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ["-create_date"]

    @classmethod
    def search_by_name(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business


class Notices(models.Model):
    title = models.CharField(max_length=20)
    post_date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-post_date']
