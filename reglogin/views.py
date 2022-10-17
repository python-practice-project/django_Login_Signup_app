from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
'''from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic'''

# Create your views here.
def index(request):
    return render(request, 'index.html')

'''class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "index.html"'''

def login(request):
    return render(request, 'login.html')
