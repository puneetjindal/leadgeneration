from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(max_length=200, blank=True, null=True)
    client_poc_name = models.CharField(max_length=200)
    title = models.CharField(max_length=5, blank=True, null=True)
    contact_number = models.BigIntegerField(blank=True, null=True)
    email_id = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    channel = models.CharField(max_length=100)
    spm = models.PositiveIntegerField(default=0)
    expected_spm = models.PositiveIntegerField(default=0)
    primary_owner = models.ForeignKey(User, blank=True, null=True,
        related_name='+')
    secondary_owner = models.ForeignKey(User, blank=True, null=True,
        related_name='+')

    class Meta:
        verbose_name = 'Lead Generation'
