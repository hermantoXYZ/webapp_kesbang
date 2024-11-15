from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_staff = models.BooleanField('Is staff', default=False)
    is_pelanggan = models.BooleanField('Is pelanggan', default=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='profile_images', blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
