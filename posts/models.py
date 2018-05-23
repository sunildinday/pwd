from django.db import models

# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField
class feed(models.Model):
    id=models.IntegerField(primary_key=True)
    author=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    description=RichTextUploadingField(blank=True,null=True)
    body=models.TextField()
