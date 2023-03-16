from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .forms import CustomUserCreationForm

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')
    

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username or password is incorrect")
        
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, "You have been logged out")
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            username = form.cleaned_data.get('username')
            user.save()

            messages.success(request, "Account was created for " + username)

            login(request, user)
            return redirect('login')
        else:
            messages.error(request, "An error has occurred during registration")
        
    context = {
                'page': page,
                'form': form
               }
    return render(request, 'users/login_register.html', context)


def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }

    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="") # Exclude skills with no description
    otherSkills = profile.skill_set.filter(description__exact="") # Include skills with no description

    context = {
        'profile': profile,
        'topSkills': topSkills,
        'otherSkills': otherSkills
    }

    return render(request, 'users/user-profile.html', context)
