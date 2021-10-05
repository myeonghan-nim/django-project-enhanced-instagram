from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from account.models import User
from .forms import PostForm, CommentForm
from .models import Post, HashTag, Comment


def index(request):
    context = {
        'posts': Paginator(Post.objects.all(), 6).get_page(request.GET.get('page')),
        'comments': Comment.objects.all(),
        'comment_form': CommentForm(),
    }
    return render(request, 'post/index.html', context)


def hashtags(request, hashtag_id):
    hashtag = get_object_or_404(HashTag, id=hashtag_id)
    context = {
        'posts': hashtag.taged_post.all(),
        'comments': Comment.objects.all(),
        'comment_form': CommentForm(),
    }
    return render(request, 'post/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            for word in post.content.split():
                if word.startswith('#'):
                    post.hashtags.add(
                        HashTag.objects.get_or_create(content=word)[0])
            return redirect('post:index')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)


@login_required
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save()
                post.hashtags.clear()
                for word in post.content.split():
                    if word.startswith('#'):
                        post.hashtags.add(
                            HashTag.objects.get_or_create(content=word)[0])
                return redirect('post:index')
        else:
            form = PostForm(instance=post)

        context = {
            'form': form,
        }

        return render(request, 'post/form.html', context)

    return redirect('post:index')


@login_required
def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user:
        post.delete()
    return redirect('post:index')


@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)

    return redirect('post:index')


def search(request):
    context = {
        'posts': Paginator(
            Post.objects.filter(Q(content__contains=request.GET.get('search'))), 6).get_page(request.GET.get('page')),
        'comments': Comment.objects.all(),
        'comment_form': CommentForm(),
    }
    return render(request, 'post/index.html', context)
