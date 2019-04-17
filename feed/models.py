from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Republic(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now)
    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-date"]


class Indiatoday(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now)
    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-id"]


class Ndtv(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now)

    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-id"]


class Hindustan(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-id"]


class Thehindu(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now)
    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-id"]


class Zeenews(models.Model):
    headline = models.TextField(null=False)
    link = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now)
    category = models.TextField(null=True)
    sentiment = models.TextField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["-id"]


class IndexTop10(models.Model):
    db_keyword = models.TextField(null=False)
    db_frequency = models.PositiveIntegerField(null=False, default=0)
