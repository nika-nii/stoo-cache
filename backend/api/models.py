from django.db import models
from datetime import datetime
REVIEW_TARGET_TYPES = [
    ("tch", "Преподаватель"),
    ("sbj", "Предмет"),
]
    

class ReviewTarget(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=3, choices=REVIEW_TARGET_TYPES)


class Group(models.Model):
    name = models.CharField(max_length=100)


class Review(models.Model):
    text = models.CharField(max_length=1000)
    rating = models.IntegerField()
    target = models.ForeignKey(ReviewTarget, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())