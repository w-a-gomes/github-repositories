# from django.http import HttpResponse
import requests

from django.shortcuts import render, redirect
from .models import GitRepo

def index(request):
	return render(request, 'searchapp/index.html', {})


def saved(request):
    return render(request, 'searchapp/saved.html', {})


def infosave(request):
    return render(request, 'searchapp/infosave.html', {})


def inforemove(request):
    return render(request, 'searchapp/inforemove.html', {})
