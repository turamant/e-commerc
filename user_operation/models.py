from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods

# Create your models here.
User = get_user_model()


class UserFav(models.Model):
    """
User Favorites
    """
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name="commodity", help_text="Commodity id", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add time")

    class Meta:
        verbose_name = 'User Collection'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.username


class UserLeavingMessage(models.Model):
    """
User Comments
    """
    MESSAGE_CHOICES = (
        (1, "leave a message"),
        (2, "Complaint"),
        (3, "ask"),
        (4, "After Sales"),
        (5, "Buy")
    )
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="Message Type",
                                       help_text=u'Message type: 1 (message), 2 (complaint), 3 (inquiry), 4 (after sale), 5 (buy)')
    subject = models.CharField(max_length=100, default="", verbose_name="Theme ")
    message = models.TextField(default="", verbose_name="Message content", help_text="Message content")
    file = models.FileField(upload_to="message/images/", verbose_name="Uploaded file", help_text="Uploaded file")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = "User Comments"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserAddress(models.Model):
    """
User delivery address
    """
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    province = models.CharField(max_length=100, default="", verbose_name="Province ")
    city = models.CharField(max_length=100, default="", verbose_name="city")
    district = models.CharField(max_length=100, default="", verbose_name="Area ")
    address = models.CharField(max_length=100, default="", verbose_name="Address")
    signer_name = models.CharField(max_length=100, default="", verbose_name="Signee ")
    signer_mobile = models.CharField(max_length=11, default="", verbose_name="Phone ")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = "Shipping address"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address
