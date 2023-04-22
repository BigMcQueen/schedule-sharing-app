from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    schedule_date = models.DateField()

    def __str__(self):
        return self.title
