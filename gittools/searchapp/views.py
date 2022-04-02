# from django.http import HttpResponse
import requests

from django.shortcuts import render, redirect
from django.utils import timezone

from .models import GitRepo


def index(request):
    programming_lang = None
    git_response = []

    if request.method == 'POST':

        if 'search_lang_button_pressed' in request.POST:
            if 'programming_lang' in request.POST:
                programming_lang = request.POST['programming_lang']

                if programming_lang != 'None':
                    url = (
                        'https://api.github.com/search/repositories?q=language:{}&sort=stars'
                        .format(programming_lang)
                    )
                    response = requests.get(url)
                    response_dict = response.json()

                    # Show all keys | {'items': [{}, {}, {}], ...}
                    # for i in git_response_dict['items'][0].keys():
                    #     print(i)

                    for repo in response_dict['items']:
                        if repo['description']:
                            description = repo['description'] if len(repo['description']) < 75 else repo['description'][:72] + '...'
                        else:
                            description = 'Without description'
                        
                        git_response.append({
                            'id': repo['id'],
                            'name': repo['name'],
                            'stargazers_count': repo['stargazers_count'],
                            'description': description,
                            'html_url': repo['html_url'],
                        })

    return render(
        request,
        'searchapp/index.html',
        {
            'programming_lang': programming_lang,
            'git_response': git_response,
            'repo_save': False,
            'existing_repositories': [x.name for x in GitRepo.objects.all()],
        }
    )


def infosave(request):
    repo_save = False
    existing_repositories = [x.name for x in GitRepo.objects.all()]

    if request.method == 'POST':
        if 'save_button_pressed' in request.POST:

            for request_post in request.POST:
                if 'repository✱' in request_post[:len('repository✱')]:
                    _prefix, repo_id, repo_name, repo_lang, repo_description, repo_stargazers_count, repo_html_url = request_post.split('✱')
                    
                    # Check duplicates and save
                    if repo_name not in existing_repositories:
                        gr = GitRepo(
                            name=repo_name,
                            _id=int(repo_id),
                            lang=repo_lang,
                            description=repo_description,
                            stargazers_count=repo_stargazers_count,
                            html_url=repo_html_url,
                            pub_date=timezone.now())
                        gr.save()
                        repo_save = True
                    
            return render(request, 'searchapp/infosave.html', {
                'repo_save': repo_save,
                'existing_repositories': existing_repositories,
            })

    # return render(request, 'searchapp/infosave.html', {})
    return redirect(index)


def saved(request):
    # existing_repositories = [(x.name, x.lang) for x in GitRepo.objects.all()]
    existing_repositories = []
    for language in ['C', 'Elixir', 'PHP', 'Python', 'Rust']:
        for repo in GitRepo.objects.all():
            if repo.lang == language:
                space_decoration = ('__________')[:10 - len(repo.lang)]
                space_description = '_' * 11
                description = repo.description if len(repo.description) < 60 else repo.description[:57] + '...'
                existing_repositories.append(
                    {
                        'id': repo.id,
                        'lang': repo.lang,
                        'space_decoration': space_decoration,
                        'name': repo.name,
                        'space_description': space_description,
                        'description': description,
                        'stargazers_count': repo.stargazers_count,
                        'html_url': repo.html_url,
                    }
                )

    return render(request, 'searchapp/saved.html', {
        'existing_repositories': existing_repositories,
    })


def inforemove(request):
    repo_remove = False
    if request.method == 'POST':
        if 'remove_button_pressed' in request.POST:

            for request_post in request.POST:
                if 'repository✱' in request_post[:len('repository✱')]:
                    _repository_prefix, repository_name = request_post.split('✱')

                    # Remove
                    gr = GitRepo.objects.get(name=repository_name)
                    gr.delete()
                    repo_remove = True

    return render(request, 'searchapp/inforemove.html', {
        'repo_remove': repo_remove,
    })
