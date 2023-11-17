from django.db import models


# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, default='')
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    massage = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]


def __str__(self):
    return "{} - {} - {}".format(self.name, self.last_name, self.id)
