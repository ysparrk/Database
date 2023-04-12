from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
#
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from .forms import CustomUserCreationForm, CustomUserChangeForm



# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index') 
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['POST'])
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index') 
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'accounts/update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index') 
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'accounts/change_password.html', context)

# 프로필
def profile(request, username):
    # User = get_user_model()
    # person = User.objects.get(username=username)
    person = get_user_model().objects.get(username=username)

    context = {
        'person' : person
    }
    return render(request, 'accounts/profile.html', context)

# 팔로우
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated: # 로그인 한 사람만 follow 가능
        # User = get_user_model()
        # person = User.objects.get(pk=user_pk)
        person = get_user_model().objects.get(pk=user_pk) # request한 사람이 본인이 아니어야 한다
        
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists(): # 이미 팔로우 한 사람
                person.followers.remove(request.user) # 언팔
            else:
                person.followers.add(request.user) # 팔로우
        return redirect('accounts:profile', person.username) # 팔로우한 사람의 프로필로 이동
    return redirect('accounts:login')