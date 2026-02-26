from django.db import models

class Category(models.Model):
    RCU_CHOICES = [
        (0, 'Inactive'),
        (1, 'Active'),
    ]
    
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    scheme = models.CharField(max_length=50, blank=True, null=True)  # optional field
    status = models.IntegerField(choices=RCU_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

