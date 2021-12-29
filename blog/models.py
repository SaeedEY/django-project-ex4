from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    tags = [    ('Tech', 'Tech'),
                ('World', 'World'),
                ('CryptoCurrency', 'Crypto Currencies'),
                ('NewScience', 'New Sciences')
    ]
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    media = models.URLField(default='')
    tag = models.CharField(max_length=32,default='Te',choices=tags)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Setting(models.Model):
    uid = models.AutoField(primary_key=True)
    option = models.CharField(unique=True,max_length=32,choices=[('blog_title','Blog Title'),('blog_about','Blog About'),('blog_social_media','Blog Social Media')])
    value = models.TextField(max_length=128,default=None)

# Create your models here.
