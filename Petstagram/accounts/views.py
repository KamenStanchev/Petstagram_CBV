from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import forms, authenticate, login, logout


def create_accout(request):
    form = forms.UserCreationForm()

    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created with username: ' + user)
            return redirect('login_page')

    context = {'form': form, }
    return render(request, 'create_account.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User was successful log-in')
            return redirect('dashboard')
        else:
            messages.error(request, 'User or passwowrd is invalid')

    form = forms.AuthenticationForm
    context = {'form': form, }
    return render(request, 'login_page.html', context)


def logout_page(request):
    logout(request)
    messages.success(request, 'User was successful LogOut')
    return redirect('login_page')

def account_details():
    pass


def edit_profile():
    pass


def edit_password():
    pass
