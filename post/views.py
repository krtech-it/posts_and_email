from django.shortcuts import render, redirect
from .models import Post
from django.core.mail import send_mail


def view_home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {"posts": posts})


def add_like(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return redirect("home")
    post.likes += 1
    post.save()
    send_mail(
        subject="Лайк +1",
        message=f"{post.__str__()} +1 лайк \n{str(post.updated)}",
        from_email=None,
        recipient_list=[post.author.email],
        fail_silently=False
    )
    return redirect("home")

# Create your views here.
