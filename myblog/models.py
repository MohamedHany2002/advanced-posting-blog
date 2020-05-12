from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse
from taggit.managers import TaggableManager




# Create your models here.


class published_manager(models.Manager):
    def get_queryset(self):
        return super(published_manager,self).get_queryset().filter(status='published')

class comment_manager(models.Manager):
    def get_queryset(self):
        return super(comment_manager,self).get_queryset().filter(active=True)



class post(models.Model):
    status_choices=(('draft','Draft'),
    ('published','Published'),
    )
    title=models.CharField(max_length=100)
    body=models.TextField()
    slug=models.SlugField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    publish=models.DateTimeField(default=timezone.now)
    auther=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    status=models.CharField(default='draft',choices=status_choices,max_length=50)
    objects=models.Manager()
    published_posts=published_manager()
    tags=TaggableManager()
  




    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})





class comment(models.Model):
    text=models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comments')
    created=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(post,on_delete=models.CASCADE,related_name='post_comments')
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    active_comments=comment_manager()
    objects=models.Manager()

    

    def __str__(self):
        return self.user.username + ' '+ self.text[:30] 

    class Meta:
        ordering=('-created',)