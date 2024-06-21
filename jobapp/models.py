from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    description = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)
    closing_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #string representaion of an object, what to display after querying post
    def __str__(self):
        return self.job_title

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_image = models.ImageField(null=False, blank=False, upload_to='images/')
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    bio = models.CharField(max_length=100, blank=True)
    resume = models.FileField(upload_to='resume', null=True, blank=True)

    def __str__(self):
        return self.firstname
