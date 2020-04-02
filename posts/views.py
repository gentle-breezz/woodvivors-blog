from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def post_list(request):
    #recupera i post dal database e li ordina
    posts = Post.objects.all().order_by('date')
    #chiama template e passa i post in un dizionario
    return render(request, 'posts/post_list.html',{'posts':posts})

def post_detail(request, slug):
    # return HttpResponse(slug)
    post = Post.objects.get(slug=slug)
    return render(request,'posts/post_singolo.html',{'post':post})

@login_required(login_url="/accounts/login/")
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post_instance = form.save(commit=False)
            post_instance.author = request.user
            post_instance.save()
            return redirect('posts:lista_post')
    else:
        form = forms.CreatePost()
    return render(request,'posts/post_create.html',{'form':form})
