from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    elif request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            messages.error(request, 'Username OR password is incorrect')
    return render(request, 'account/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def registration_view(request):
    if request.user.is_authenticated:
        return redirect('main_page')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = UserCreationForm()

    return render(request, 'account/registration.html', {'form': form})