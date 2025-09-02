from django.db import models
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
# Create your models here.

CATEGORIES = [
    ('Food', 'Food'),
    ('Transport', 'Transport'),
    ('Shopping', 'Shopping'),
    ('Utilities', 'Utilities'),
    ('Other', 'Other'),
]

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    category = models.CharField(max_length=50, choices=CATEGORIES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # add for once
    updated_at = models.DateTimeField(auto_now=True) # every time when the user changes expense data
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.description}"