from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View

from accounts.forms import CustomLoginForm, RegisterForm
from events.models import Event


def home_page(request):
    now = timezone.now()
    active_hackathons = Event.objects.filter(is_approved=True,
                                             start_date__lt=now,
                                             end_date__gt=now)
    past_hackathons = Event.objects.filter(is_approved=True,
                                           end_date__lt=now)
    upcoming_hackathons = Event.objects.filter(is_approved=True,
                                               start_date__gt=now)
    context = {
        'active_hackathons': active_hackathons,
        'upcoming_hackathons': upcoming_hackathons,
        'past_hackathons': past_hackathons,
    }
    return render(
        request, 'home.html', context
    )


class LoginView(View):
    def get(self, request):
        form = CustomLoginForm()
        return render(request, 'accounts/login.html', context={'form': form})

    def post(self, request):
        form = CustomLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home_page')
            else:
                return HttpResponse("Username or password is wrong!!!")
        return render(request, 'accounts/login.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('home_page')


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        return render(request, 'accounts/register.html', context={'form': form})
