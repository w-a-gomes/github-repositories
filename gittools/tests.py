from django.test.utils import setup_test_environment
from django.test import Client, TestCase
from django.urls import reverse


# Setup
setup_test_environment() 


class TestViews(TestCase):
    """"""

    client = Client()

    def test_index(self):
        response = self.client.get(reverse('searchapp:index'))

        # >>> response.content
        # b'<html>...'
        # >>> response.context['latest_question_list']
        # <QuerySet [<Question: What's up?>]>

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'index.html')

    def test_saved(self):
        response = self.client.get(reverse('searchapp:saved'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'saved.html')

# python manage.py test app