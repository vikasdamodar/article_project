from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class BlogArticle(models.Model):
    """ Article data """
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_datetime = models.DateTimeField()
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
