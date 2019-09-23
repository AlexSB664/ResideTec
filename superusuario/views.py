from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)