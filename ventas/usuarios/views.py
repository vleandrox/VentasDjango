from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrarUsuario

def registrar(request):
	if request.method == 'POST':
		form = RegistrarUsuario(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('login')
	else:
		form= RegistrarUsuario()
	return render(request,'usuario/registrar.html',{'form':form})