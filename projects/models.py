from django.db import models
import uuid
from users.models import Profile


class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='projects')
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default = 'default.jpg')
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True,)
    votes_total = models.IntegerField(default=0, null=True, blank=True)
    votes_ratio = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created_at']

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    #owner = 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    

    def __str__(self):
        return self.name

    