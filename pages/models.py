from django.db import models


# Create your models here.
class Member(models.Model):  # member in the team
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    linkedin_link = models.URLField(max_length=100)
    github_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
