from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now



# Create your models here.
class Contact(models.Model):
    Firstname = models.CharField(max_length=100,null=True)
    Lastname = models.CharField(max_length=100,null=True)
    profilepicture =models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,null=True )
    username =models.CharField(max_length=100,null=True)
    email =models.CharField(max_length=100,null=True)
    address =models.CharField(max_length=100,null=True)
    address2 =models.CharField(max_length=100,null=True)
    city =models.CharField(max_length=100,null=True)
    state =models.CharField(max_length=100,null=True)
    zip =models.CharField(max_length=100,null=True)
    
    
class Contact_1(models.Model):
    Firstname = models.CharField(max_length=100,null=True)
    Lastname = models.CharField(max_length=100,null=True)
    profilepicture =models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,null=True )
    username =models.CharField(max_length=100,null=True)
    email =models.CharField(max_length=100,null=True)
    address =models.CharField(max_length=100,null=True)
    address2 =models.CharField(max_length=100,null=True)
    city =models.CharField(max_length=100,null=True)
    state =models.CharField(max_length=100,null=True)
    zip =models.CharField(max_length=100,null=True)

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

class BlogPost(models.Model):
    title=models.CharField(max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.CharField(max_length=130)
    category=models.CharField(max_length=100,null=True)
    content=models.TextField(max_length=100,null=True)
    summury=models.CharField(max_length=15,null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    dateTime=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title
    
    def get_absolute_url(self):
        return reverse('blogs')
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
    dateTime=models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username +  " Comment: " + self.content
    

