
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    model = CustomUser
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class PasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'


class PasswordChangeSuccessView(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'
