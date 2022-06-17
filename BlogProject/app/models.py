from django.db import models
# from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here.


class Contact(models.Model):
    # contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122, default = None)
    # phone = models.CharField(max_length=12, blank=True )
    message = models.TextField(null=False, default = None)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

# Category Model

# Post Model

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    url = models.CharField(max_length=50)
    # cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured = models.BooleanField(null=True)
    add_date = models.DateTimeField(auto_now=True, null=True)
    image = models.ImageField(upload_to="post/")

    def __str__(self):
        return self.title


