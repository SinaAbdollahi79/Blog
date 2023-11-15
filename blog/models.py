from django.db import models


# Create your models here.
class post(models.Model):
    titel = models.CharField(max_length=100)
    content = models.TextField()
    conted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_date']
        

    def __str__(self):
        return "{} - {}".format(self.titel, self.id)
