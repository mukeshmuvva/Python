from django.db import models

# Create your models here.
class Testimonial(models.Model):
    def __str__(self):
        return self.username+": "+self.description
    username=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    description=models.CharField(max_length=250)


class Feedback(models.Model):
    def __str__(self):
            return self.Email+": "+self.review
    Email = models.CharField(max_length=75)
    rating=models.IntegerField()
    review = models.TextField()
