from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from article.models import BlogArticle
from article.serializers import ArticleSerializer


class ArticleList(ListAPIView):
    pagination_class = PageNumberPagination
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'article_list.html'
    queryset = BlogArticle.objects.filter(is_published=True).order_by('id')
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        """ List all published articles"""
        response = self.list(request, *args, **kwargs)
        return Response(
            {
                'articles': response.data.get('results'),
                'next': response.data.get('next'),
                'previous': response.data.get('previous')
            }
        )


class ArticleDetail(RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'article_detail.html'
    queryset = BlogArticle.objects.filter(is_published=True)
    lookup_fields = ["id", "slug"]

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        for field in self.lookup_fields:
            filter_kwargs = {field: self.kwargs[field]}
            queryset = queryset.filter(**filter_kwargs)
        return queryset.get()

    def get(self, request, *args, **kwargs):
        """ Fetch Article details"""
        return Response({'article': self.get_object()})
