from django.db import models


class apt(models.Model):
    apt_name = models.CharField(max_length=100)

    def __str__(self):
        return self.apt_name
