# 写文章的表单类
from django.forms import ModelForm

from article.models import ArticlePost


class ArticlePostForm(ModelForm):
    class Meta:
        # 指明数据模型来源
        model = ArticlePost
        # 定义表单包含的字段
        fields = ('title', 'body')
