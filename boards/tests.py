from django.test import TestCase, Client
from django.urls import resolve, reverse
from . import views
from . import models
# Create your tests here.
class HomeTests(TestCase):
    def setUp(self):
        self.board = models.Board.objects.create(name="Django", description="Django Board")
        c = Client()
        url = reverse("index")
        self.response = c.get(url)

    def test_index_view(self):
        c = Client()
        response = c.get('/')
        self.assertEquals(response.status_code, 200)

    def test_index_view_url_resolve_index(self):
        view = resolve("/")
        self.assertEquals(view.func, views.index)

    def test_index_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'id': self.board.id})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))

class BoardTopicsTest(TestCase):
    def setUp(self):
        models.Board.objects.create(name="Django", description="Django Board")
    
    def test_board_topics_view_success_code(self):
        url = reverse('board_topics', kwargs={'id': 1})
        c = Client()
        response = c.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_failure_code(self):
        url = reverse('board_topics', kwargs={'id': 99})
        c = Client()
        response = c.get(url)
        self.assertEquals(response.status_code, 404)
    
    def test_board_topics_url_resolve_board_topics(self):
        view = resolve("/boards/1")
        self.assertEquals(view.func, views.board_topics)

    def test_board_topics_contains_link_back_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'id': 1})
        c = Client()
        response = c.get(board_topics_url)
        index_url = reverse('index')
        self.assertContains(response, "href='{0}'".format(index_url))