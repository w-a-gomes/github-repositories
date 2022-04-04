import requests

from django.test import TestCase
from django.urls import reverse

from ..views import index_get_git_response_items


class ListTests(TestCase):
    """"""
    response = index_get_git_response_items(
        requests.get(
            'https://api.github.com/search/repositories?' +
            'q=language:Python&sort=stars'
        ).json()
    )

    def test_keys(self):
        """"""
        for repo in self.response:
            self.assertIn('id', repo)
            self.assertIn('name', repo)
            self.assertIn('stargazers_count', repo)
            self.assertIn('description', repo)
            self.assertIn('html_url', repo)


class CListTests(TestCase):
    """"""
    def test_elixir_repos(self):
        response = index_get_git_response_items(
            requests.get(
                'https://api.github.com/search/repositories?' +
                'q=language:Elixir&sort=stars'
            ).json()
        )
        repo_list = []
        for repo in response:
            repo_list.append(repo['name'])

        self.assertIn('elixir', repo_list)
