from django.shortcuts import render, redirect
from .forms import InscriptionForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
    user = request.user
    return render(request, 'intrococo/connexion/home.html', {'user': user})

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = InscriptionForm()
    return render(request, 'intrococo/connexion/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "pas bon"
            return render(request, 'intrococo/connexion/connexion.html', {'error': error})
    return render(request, 'intrococo/connexion/connexion.html')

def deco(request):
    logout(request)
    return redirect('home')