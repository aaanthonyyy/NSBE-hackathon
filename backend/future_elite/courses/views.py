from django.http import Http404
from django.shortcuts import render

def index(request):
    
    return render(request, 'courses/')
# Leave the rest of the views (detail, results, vote) unchanged