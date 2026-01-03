from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):

    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Rent', 'Rent'),
        ('Shopping', 'Shopping'),
        ('Bills', 'Bills'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Other'   # ✅ ensures old data doesn’t break
    )
    date = models.DateField()

    def __str__(self):
        return self.title
