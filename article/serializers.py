from rest_framework.serializers import ModelSerializer

from article.models import BlogArticle


class ArticleSerializer(ModelSerializer):
    class Meta:
        """ Meta data"""
        model = BlogArticle
        fields = ['id', 'title', 'slug']
