from django.shortcuts import render
from django.views.generic import DetailView
from django.shortcuts import render, redirect
from django.urls import reverse

# Models
from django.contrib.auth.models import User


# Create your views here.
class UserDetailView(DetailView):
    """ User Detail View """

    template_name = 'userpublic.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'
