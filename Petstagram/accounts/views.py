from django.shortcuts import render, redirect
from django.contrib.auth import forms


def create_accout(request):
    form = forms.UserCreationForm()

    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {'form': form,}
    return render(request, 'create_account.html', context)


def login_page():
    pass


def account_details():
    pass


def edit_profile():
    pass


def edit_password():
    pass
