from django import forms
from .models import Article, Comment

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     content = forms.CharField(widget=forms.Textarea)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # 출력 필드 수정 -> title과 content만 보여지게 한다.
        fields = ('title', 'content',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('article',)
