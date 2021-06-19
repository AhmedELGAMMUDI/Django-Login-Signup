from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserCreateForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
       
        if form.is_valid():
            
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('index')
      
    else:
        form = UserCreateForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def index(request):
    return render(request,'index.html',{})



