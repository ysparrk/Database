from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    # article 모델에 user 모델을 참조하는 외래 키 작성
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'

class Comment(models.Model):
    # comment는 어떤 article의 comment인지 알려주어야 한다.
	# article 필드는 ForeignKey 필드 -> 자동적으로 article의 id를 가리킨다.
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    
    