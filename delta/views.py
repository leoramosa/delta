"""Delta views."""

# django
from django.http import HttpResponse
from django.views.generic import TemplateView
# utilities
from datetime import datetime
import json


class Home(TemplateView):
    template_name = 'home.html'
