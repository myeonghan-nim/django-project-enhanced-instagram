from django.shortcuts import render, redirect, get_object_or_404
from auth.models import User

from .forms import PostForm, CommentForm
from .models import Post, HashTag, Comment

from django.contrib.auth.decorators import login_required

from django.db.models import Q

from django.core.paginator import Paginator

# Create your views here.


def index(request):

    posts = Post.objects.all()
    comments = Comment.objects.all()

    comment_form = CommentForm()

    paginator = Paginator(posts, 6)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'posts': posts,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'posts/index.html', context)


def hashtags(request, hashtag_id):

    hashtag = get_object_or_404(HashTag, id=hashtag_id)
    posts = hashtag.taged_post.all()
    comments = Comment.objects.all()

    comment_form = CommentForm()

    context = {
        'posts': posts,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'posts/index.html', context)


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
                    hashtag = HashTag.objects.get_or_create(content=word)[0]
                    post.hashtags.add(hashtag)

            return redirect('posts:index')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'posts/forms.html', context)


@login_required
def update(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if post.user == request.user:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)

            if form.is_valid():

                post = form.save()
                post.hashtags.clear()

                for word in post.content.split():
                    if word.startswith('#'):
                        hashtag = HashTag.objects.get_or_create(content=word)[
                            0]
                        post.hashtags.add(hashtag)

                return redirect('posts:index')
        else:
            form = PostForm(instance=post)

        context = {
            'form': form,
        }

        return render(request, 'posts/forms.html', context)

    return redirect('posts:index')


@login_required
def delete(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if post.user == request.user:
        post.delete()

    return redirect('posts:index')


@login_required
def like(request, post_id):

    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)

    return redirect('posts:index')


def search(request):

    target = request.GET.get('search')
    posts = Post.objects.filter(Q(content__contains=target))

    context = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)
