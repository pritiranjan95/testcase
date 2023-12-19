from django.db import models
import uuid

class Signup(models.Model):
    Name=models.CharField(max_length=200)
    Email_id=models.CharField(max_length=400)
    password=models.CharField(max_length=300) 
    user_id=models.UUIDField(default=uuid.uuid4, editable=False)
