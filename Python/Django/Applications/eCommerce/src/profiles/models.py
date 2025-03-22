from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=1200)
    description = models.TextField(default='description default')

    def __str__(self):
        return self.name
