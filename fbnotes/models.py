from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    username = models.CharField(max_length=20)
    document_id = models.IntegerField(null=False)
    title = models.CharField(max_length=500)
    contents = models.CharField(max_length=5000)
    
    class Meta:
        unique_together = (('username', 'document_id'),)

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    document_id = models.IntegerField()
