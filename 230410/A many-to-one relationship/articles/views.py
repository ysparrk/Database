from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # article의 모든 comment들 조회(역참조)
    comments = article.comment_set.all()
    context = {
        'article' : article,
        'comment_form' : comment_form,
        'comments' : comments,  # context에 담는다.
    }
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # 게시글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit옵션 활용
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
    if request.user.is_authenticated:
        if request.user == article.user:  # 삭제 요청자 == 게시글 작성자
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)  # else라면 현재 페이지에 머무르기


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:  # 수정 요청자 == 게시글 작성자
        if request.method == 'POST': # 수정 가능
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', pk=article.pk)
        else:
            form = ArticleForm(instance=article)
    
    else:
        return redirect('articles:index')  # else라면 index페이지로 돌아가기
    
    context = {'form': form, 'article': article}
    return render(request, 'articles/update.html', context)

#================ COMMENTS ============================
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False) # 인스턴스를 comment에 담는다
        comment.article = article  # 가져온 article을 담아준다
        comment.save()  # 데이터가 다 채워져서 save

        # comment_form.save() 
        # article에 대한 데이터를 comment에 넣는 것이 없다.
        # 실제로 db에 save하기 전에 comment 인스턴스에 접근하는 것이 필요하다. 저장하기 전에 필요한 article을 채워준다 
        # save를 하긴 하지만 DB에 반영하지 않는 단계가 필요하다
    return redirect('articles:detail', article.pk)


def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)  # comment 가져와서 지워준다.
    comment.delete() 
    return redirect('articles:detail', article_pk)



 