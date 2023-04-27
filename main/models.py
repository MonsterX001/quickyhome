from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.CharField(max_length=100000000)
    agentname = models.TextField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='main_images', default='blank-img.png')
    
    def __str__(self):
        return self.user.username

class Houseuploads(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.TextField(max_length=100)
    house_name = models.CharField(max_length=100)
    main_img = models.ImageField(upload_to='post_images')
    houseimg_one = models.ImageField(upload_to='post_images')
    houseimg_two = models.ImageField(upload_to='post_images')
    houseimg_three = models.ImageField(upload_to='post_images')
    houseimg_four = models.ImageField(upload_to='post_images')
    houseimg_five = models.ImageField(upload_to='post_images')
    details = models.TextField()
    housetype = models.TextField()
    location = models.CharField(max_length=100, blank=True)
    rentmonth = models.CharField(max_length=10)
    phone_no = models.IntegerField()
    def __str__(self):
        return self.user