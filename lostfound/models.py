from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class LostFoundItem(models.Model):
    STATUS_CHOICES = (
        ('lost', 'Lost'),
        ('found', 'Found'),
    )

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50,default='lost')  # 📦 New field
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_reported = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.status})"

    def get_category_url(self):
        return reverse('category_items', args=[self.category.lower()])

