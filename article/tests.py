from django.utils import timezone

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

from article.models import BlogArticle


class ArticleTC(TestCase):
    def setUp(self) -> None:
        """ Set up Test data"""
        self.user = User.objects.create(
            username="testuser", password="passs1234",
            first_name="Test", last_name="User"
        )
        self.articles = [
            BlogArticle.objects.create(
                title=f"Article {each_article}",
                content=f"Content {each_article}",
                author=self.user,
                publication_datetime=timezone.now(),
            ) for each_article in range(10)
        ]

    def test_article_slug(self):
        """ Test article slug is being updated properly"""
        self.assertEqual(self.articles[0].slug, slugify(self.articles[0].title))

    def test_article_list(self):
        """ Test Article list """
        response = self.client.get(reverse("article_list"))
        for a_data, a_obj in zip(response.data['articles'], self.articles):
            self.assertEqual(a_data['id'], a_obj.id)
            self.assertEqual(a_data['title'], a_obj.title)
            self.assertEqual(a_data['slug'], a_obj.slug)

        # next url refer to 2nd page
        self.assertEqual(response.data['next'][-1], '2')
        # prev url should be None
        self.assertIsNone(response.data['previous'])

    def test_article_detail(self):
        """ Test Article detail """
        second_article = self.articles[1]
        response = self.client.get(reverse(
            "article_detail", kwargs={'id': second_article.id, 'slug': second_article.slug}
        ))
        self.assertEqual(response.data['article'], second_article)
