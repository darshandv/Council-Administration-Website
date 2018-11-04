from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    upvote = models.IntegerField(default=0)
    implemented = models.BooleanField(default=False)
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField( blank=True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("grievance:post_list")

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete = models.CASCADE)
    parent_comment = models.ForeignKey("self", related_name='parent', on_delete = models.CASCADE, null=True, blank =True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


    def get_absolute_url(self):
        return reverse("post_list")

    def children(self): #replies
        return Comment.objects.filter(parent=self)

    def __str__(self):
        return self.text

class Event(models.Model):
    created_date = models.DateField()
    finished_date = models.DateField(null = True, blank = True)
    title = models.CharField(max_length = 50)
    text = models.CharField(max_length = 300)

    def __str_(self):
        return self.title

class TimePoint(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='timepoints')
    date = models.DateField()
    text = models.CharField(max_length = 100)

    def __str__(self):
        return self.event.title

# class Secretary(models.Model):
#     status = models.ForeignKey(Comment, on_delete=models.CASCADE)
