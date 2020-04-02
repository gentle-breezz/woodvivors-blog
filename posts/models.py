from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # Con la scelta dei field type si determina anche il tipo di widjet di
    # default che viene mostrato per inserire o modificare il tipo di dato
    # sia parte admin che user
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)
    author = models.ForeignKey(
        User,
        default=None,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:150] + '... '
