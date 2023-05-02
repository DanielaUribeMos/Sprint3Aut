from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import HistoriaForm
from .logic.historia_logic import get_historias, get_historia, create_historia
from django.contrib.auth.decorators import login_required
from windmy.auth0backend import getRole

@login_required
def historia_list(request):
    role = getRole(request)
    if role == "Doctor":
        historias = get_historias()
        context = {
            'historia_list': historias
        }
        return render(request, 'Historia/historias.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def single_historia(request, id=0):
    historia = get_historia(id)
    context = {
        'historia': historia
    }
    return render(request, 'Historia/historia.html', context)

@login_required
def historia_create(request):
    role = getRole(request)
    if role == "Doctor":
        if request.method == 'POST':
            form = HistoriaForm(request.POST)
            if form.is_valid():
                create_historia(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created historia')
                return HttpResponseRedirect(reverse('historiaCreate'))
            else:
                print(form.errors)
        else:
            form = HistoriaForm()

        context = {
            'form': form,
        }
        return render(request, 'Historia/historiaCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")
