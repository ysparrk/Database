from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {'form': form}
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', pk=article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:detail', article.pk)
    context = {'form': form, 'article': article}
    return render(request, 'articles/update.html', context)

# 로그인 해야 댓글 create 가능
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        # 댓글 작성시 작성자 정보가 함께 저장
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)


def comments_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    # 삭제 요청자와 작성자가 같으면 삭제(본인 댓글만 삭제)
    if request.user == comment.user: 
        comment.delete()
    return redirect('articles:detail', pk)


# like 기능 구현
@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated: # 로그인 한 사람만 가능
        article = Article.objects.get(pk=article_pk)
        
        # 이 article의 모든 좋아요를 누른 user중에 request한 user가 있다면(이미 누른 상태)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)  # 좋아요 취소

        else:
            article.like_users.add(request.user)  # 좋아요 목록에 더해주기
        return redirect('articles:index')  # 글 목록으로 돌아가기
    
    return redirect('accounts:login')  # 로그인 하지 않았다면 로그인 창으로 가기
