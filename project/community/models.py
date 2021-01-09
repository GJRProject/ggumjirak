from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField


# Create your models here.
# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Post(models.Model):
    postname = models.CharField(max_length=50)
    mainphoto = ResizedImageField(blank=True, null=True)
    contents = RichTextField()
    pub_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.postname

class Notice(models.Model):
    postname = models.CharField(max_length=50)
    mainphoto = ResizedImageField(blank=True, null=True)
    contents = RichTextField()
    pub_date = models.DateTimeField(default=timezone.now)
        
    def __str__(self):
        return self.postname

class Donations_Report(models.Model):
    postname = models.CharField(max_length=50)
    mainphoto = ResizedImageField(blank=True, null=True)
    contents = RichTextField()
    pub_date = models.DateTimeField(default=timezone.now)    

    def __str__(self):
        return self.postname

class History(models.Model):
    postname = models.CharField(max_length=50)
    mainphoto = ResizedImageField(blank=True, null=True)
    contents = RichTextField()
    

    def __str__(self):
        return self.postname

class Project(models.Model):
    postname = models.CharField(max_length=50)
    mainphoto = ResizedImageField(upload_to='images/', blank=True, null=True)
    pub_date = models.DateTimeField(default=timezone.now)    

    def __str__(self):
        return self.postname

class News(models.Model):
    postname = models.CharField(max_length=50)
    mainphoto = ResizedImageField(upload_to='images/', blank=True, null=True)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.postname

class Round(models.Model):
    postname = models.CharField(max_length=50)
    mainphoto = ResizedImageField(upload_to='images/', blank=True, null=True)
    

    def __str__(self):
        return self.postname