from django.test import TestCase, Client
from django.urls import resolve, reverse
from . import views
from . import models
# Create your tests here.
class HomeTests(TestCase):
    def test_index_view(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_view_url_resolve_index(self):
        view = resolve("/")
        self.assertEqual(view.func, views.index)