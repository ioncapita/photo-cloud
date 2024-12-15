from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.title
