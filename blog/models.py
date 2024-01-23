from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class post(models.Model):
    titel = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to="blog/", default="blog/default.png")
    category = models.ManyToManyField(categories)
    conted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return "{} - {}".format(self.titel, self.id)
    
    def get_absolute_url(self):
        return reverse('blog:blog-single', kwargs={'pid': self.id})

class comment(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=250)
    approved = models.BooleanField(default=False)
    create_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
