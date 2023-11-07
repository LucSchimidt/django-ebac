from django.test import TestCase, Client
from django.urls import reverse, resolve


class TestViews(TestCase):

    def setUp(self):
        self.c = Client()
        self.response = self.c.get('/blog/')
    
    #Testando se temos um código 200 na response da view.
    def test_view_blog_response_code(self):
        self.assertEquals(self.response.status_code, 200)

    #Testando se temos um 'Hello World' no content da response:
    def test_view_blog_response_content(self):
        self.assertEquals(self.response.content, b'Hello World.')

