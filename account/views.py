from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'account/form.html', context)


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:userpage', user_id=request.user.id)
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'account/form.html', context)


def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('account:userpage', user_id=request.user.id)
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form,
    }

    return render(request, 'account/form.html', context)


def delete(request, user_id):
    if request.user == get_object_or_404(User, id=user_id):
        request.user.delete()
    return redirect('post:index')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('post:index')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'account/form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('post:index')


def userpage(request, user_id):
    context = {
        'user_info': get_object_or_404(User, id=user_id),
    }
    return render(request, 'account/userpage.html', context)


@login_required
def follow(request, user_id):
    following = get_object_or_404(User, id=user_id)
    follower = request.user

    if follower != following:
        if follower in following.followers.all():
            following.followers.remove(follower)
        else:
            following.followers.add(follower)

    return redirect('account:userpage', user_id)
