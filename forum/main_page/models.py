from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Subject.Status.PUBLISHED)


class Subject(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
             
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE, 
                               related_name='subject_name')
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    publish = models.DateField(default=timezone.now)
    created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10,
                              choices=Status.choices,
                              default=Status.PUBLISHED)
    objects = models.Manager()
    published = PublishedManager()
    liked = models.ManyToManyField(User, blank=True, through='Like')
    category = models.ForeignKey('Category', blank=True, on_delete=models.PROTECT)
    
    class Meta:
        ordering = ('-publish',)
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
    
    def num_likes(self):
        return self.liked.all().count()

    def get_absolute_url(self):
        return reverse('main_page:subject_detail', 
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
    
class Comment(models.Model):
    subject = models.ForeignKey(Subject, 
                                on_delete=models.CASCADE,
                                related_name='comments')
    name = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comment_user')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.subject}'
    

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    
    def __str__(self):
        return f"{self.user}-{self.subject}-{self.value}"
    

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'Категория - {self.name}'
    
    class Meta:
        verbose_name = verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']