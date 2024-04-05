from django.db import models


# Create your models here.
class FileName(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    key = models.CharField(max_length=200, null=True, blank=True)
    word = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.name}-{self.pk}'


class SheetName(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.name}-{self.pk}'
