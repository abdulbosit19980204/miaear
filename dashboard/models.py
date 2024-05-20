from django.db import models


# Create your models here.

class entities(models.Model):
    telegram_id = models.IntegerField(default=0)
    hash = models.IntegerField()
    username = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=2000, blank=True, null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name.__str__()
