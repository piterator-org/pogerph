from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse


class Category(models.Model):
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def get_absolute_url(self):
        return reverse('post', args=(self.slug,))

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True, blank=True)
    pub_date = models.DateTimeField(verbose_name='date published',
                                    auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    markup = models.SlugField(choices=[
        ('html', 'HTML'),
        ('md', 'Markdown'),
        ('rst', 'reStructuredText'),
        ('txt', 'Text'),
    ], default='md')
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title
