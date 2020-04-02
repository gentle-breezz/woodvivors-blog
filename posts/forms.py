from django import forms
from . import models

class CreatePost(forms.ModelForm):
 class Meta(object):
     model = models.Post
     fields = ['title','slug','body','thumb']
