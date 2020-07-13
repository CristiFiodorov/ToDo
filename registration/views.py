from django.shortcuts import render, reverse, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.info(
                request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            login(request, new_user)
        return redirect(reverse('home'))
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form": form})
