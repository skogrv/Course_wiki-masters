from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    title_tag = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('instance', args=(str(self.id)))
