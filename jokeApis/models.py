from django.db import models

class Joke(models.Model):
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    joke = models.TextField(blank=True, null=True)  # For "single" type
    flags_nsfw = models.BooleanField()
    flags_political = models.BooleanField()
    flags_sexist = models.BooleanField()
    safe = models.BooleanField()
    lang = models.CharField(max_length=10)