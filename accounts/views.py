from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm
from .services import fetch , User_data , search_profile , update

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfilesView(generic.TemplateView):
    template_name = 'registration/explore.html'
    def get_context_data(self):
        context = {
            'users' : fetch(self.request.user),
            'login_user' : self.request.user
        }
        return context

class UserView(generic.TemplateView):
    template_name = 'registration/profile.html'
    def get_context_data(self, **kwargs):
        context = {
            'current' : kwargs["id"] == self.request.user.id,
            'repos': User_data(kwargs["id"]),
            'name' : search_profile(kwargs["id"]),
            'login_user' : self.request.user
        }
        return context

class UserOwnView(generic.TemplateView):
    template_name = 'registration/profile.html'
    def get_context_data(self, **kwargs):
        context = {
            'current' : True,
            'update' : update(kwargs["id"], self.request.user),
            'repos': User_data(kwargs["id"]),
            'name' : search_profile(kwargs["id"]),
            'login_user' : self.request.user
        }
        return context