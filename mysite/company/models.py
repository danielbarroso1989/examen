from django.db import models
from django.utils import timezone
import uuid
# Create your models here Company.
class Company(models.Model):
    uuid = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True) 
    symbol = models.CharField(max_length=10, blank=True, null=True)   
    values = models.TextField(blank=True)
    created_at = models.DateField(blank=True, null=True, default=timezone.now)
