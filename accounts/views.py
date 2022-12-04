from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .forms import PerfilForm
from django.http import HttpResponse
from .models import Perfil


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

@login_required
class Cliente():

    def clienteView(request):

        if request.method == 'GET':

            return render(request,'clientes/clientes.html')



    def dadosView (request):

        if request.method == 'POST':
            form = PerfilForm(request.POST)

            if form.is_valid():
                clientes = form.save(commit=False)
                clientes.save()
                return redirect('/')


        else:
            form = PerfilForm()
            return render(request,'clientes/cadastroclientes.html',{'form':form})