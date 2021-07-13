from PIL import Image
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registered_as = models.CharField(default='Owner/Buyer', max_length=20)
    contact_number = PhoneNumberField()
    image = models.ImageField(default='default.jfif', upload_to='profile_images')

    def __str__(self):
        return f'{self.user.username} Profile'

    def formatted_phone(self):
        return str(self.contact_number)


