from django.db import models
import uuid

class Blogmodel(models.Model):
    Title= models.CharField(max_length=200)
    blog=models.CharField(max_length=4000)
    author= models.CharField(max_length=300)
    unique_id=models.UUIDField(default=uuid.uuid4, editable=False)
