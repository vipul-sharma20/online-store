from django.db import models
from django.contrib import auth
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Create auth token for new user created
    """
    if created:
        Token.objects.create(user=instance)


class Product(models.Model):
    """
    model fields for a product item
    """
    owner = models.ForeignKey('auth.User', related_name='products')
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=False)
    category = models.CharField(max_length=20, blank=True, default='')
    image = models.URLField(blank=True)

    class Meta:
        ordering = ('created',)
