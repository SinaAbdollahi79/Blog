from django.db import models

# ارتباط با ما
class contact(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, default="")
    phone_number = models.IntegerField(default=0)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    massage = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]


def __str__(self):
    return "{} - {} - {}".format(self.name, self.last_name, self.id)
