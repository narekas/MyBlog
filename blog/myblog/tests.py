from django.test import TestCase
from django.urls import resolve
from myblog.views import home_page
from django.http import HttpRequest
from myblog.models import Article
from datetime import datetime
# Create your tests here.

class HomePageTest(TestCase):

    def test_home_page_displays_articles(self):
        Article.objects.create(title='title 1',
                               summary='summary 1',
                               full_text='full_text 1',
                               pubdate=datetime.now())
        Article.objects.create(title='title 2',
                               summary='summary 2',
                               full_text='full_text 2',
                               pubdate=datetime.now())
        
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertIn('title 1', html)
        self.assertIn('sumarry 1', html)
        self.assertNotIn('full_text 1', html)
        
        self.assertIn('title 2', html)
        self.assertIn('sumarry 2', html)
        self.assertNotIn('full_text 2', html)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>Blog</title>', html)
        self.assertIn('<h1>Blog</h1>', html)  
        self.assertTrue(html.endswith('</html>'))
    

class ArticleModelTest(TestCase):

    def test_article_model_save_and_retrieve(self):
        article1 = Article(
            title = 'article 1',
            full_text = 'full_text 1',
            summary = 'summary 1',
            category = 'category 1',
            pubdate = datetime.now(),
        )
        article1.save()

        article2 = Article(
            title = 'article 2',
            full_text = 'full_text 2',
            summary = 'summary 2',
            category = 'category 2',
            pubdate = datetime.now(),
        )
        article2.save()

        all_articles = Article.objects.all()
        self.assertEqual(len(all_articles), 2)

        self.assertEqual(all_articles[0].title, article1.title)
        self.assertEqual(all_articles[1].title, article2.title)
