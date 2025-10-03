from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    if request.method == 'POST':
        request.user.email = request.POST.get('email')
        request.user.save()
    return render(request, 'auth/profile.html', {'user': request.user})
