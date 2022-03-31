from django.test import TestCase
from django.urls import reverse


class UrlViewsTests(TestCase):
    """"""
    def test_index(self):
        """"""
        response = self.client.get(reverse('searchapp:index'))

        # response.content
        # response.context
        # print(response.__dict__)

        self.assertEqual(response.status_code, 200)

    def test_saved(self):
        """"""
        response = self.client.get(reverse('searchapp:saved'))
        self.assertEqual(response.status_code, 200)

    def test_infosave(self):
        """"""
        response = self.client.get(reverse('searchapp:infosave'))
        self.assertEqual(response.status_code, 200)

    def test_inforemove(self):
        """"""
        response = self.client.get(reverse('searchapp:inforemove'))
        self.assertEqual(response.status_code, 200)
