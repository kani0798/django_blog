from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from .forms import RegistrationForm


class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/registration.html'