from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    """
Users
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Name")
    birthday = models.DateField(null=True, blank=True, verbose_name="Year of Birth")
    gender = models.CharField(max_length=6, choices=(("male", u"male"), ("female", "Female")), default="female",
                              verbose_name="gender")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="phone")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="e-mail")

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "user"

    def __str__(self):
        return self.name


class VerifyCode(models.Model):
    """
SMS verification code
    """
    code = models.CharField(max_length=10, verbose_name="Verification Code")
    mobile = models.CharField(max_length=11, verbose_name="phone")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = "SMS verification code"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code