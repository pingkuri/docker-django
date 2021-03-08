from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View

def index(request):
    return render(request, 'common/index.html', {})