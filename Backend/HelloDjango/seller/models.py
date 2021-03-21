from django.contrib.auth.models import User
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Tariff(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    coast = models.DecimalField(max_digits=5, decimal_places=2)
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE, related_name='seller')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    avatar = ThumbnailerImageField(upload_to='sellers/', resize_source={'size': (400, 400), 'crop': 'scale'},
                                   null=True, blank=True)
    balance = models.DecimalField(decimal_places=2, max_digits=5, default=2000)
    active = models.BooleanField(default=True)
    registered = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-registered',)


class Shop(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    logo = ThumbnailerImageField(upload_to='logos/', resize_source={'size': (400, 400), 'crop': 'scale'},
                                 null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)
