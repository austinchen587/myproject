from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def data_analysis(request):
    return render(request, 'data_analysis.html')

# /app/crm_backend/crm_backend/views.py
from django.http import HttpResponseNotFound
from django.shortcuts import render

def handle_not_found(request, exception):
    return render(request, '404.html', status=404)