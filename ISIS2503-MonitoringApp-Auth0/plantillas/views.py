from django.shortcuts import render
from .forms import PlantillaForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.logic_plantilla import create_plantilla, get_plantillas
from django.contrib.auth.decorators import login_required
from windmy.auth0backend import getRole

@login_required
def plantilla_list(request):
    role = getRole(request)
    if role == "Doctor" or role=="Enfermero":
        plantillas = get_plantillas()
        context = {
            'plantilla_list': plantillas
        }
        return render(request, 'Plantilla/plantillas.html', context)
    else:
        return HttpResponse("Unauthorized User")

def plantilla_create(request):
    role = getRole(request)
    if role == "Doctor" or role=="Enfermero":
        if request.method == 'POST':
            form = PlantillaForm(request.POST)
            if form.is_valid():
                create_plantilla(form)
                messages.add_message(request, messages.SUCCESS, 'Plantilla create successful')
                return HttpResponseRedirect(reverse('plantillaCreate'))
            else:
                print(form.errors)
        else:
            form = PlantillaForm()

        context = {
            'form': form,
        }

        return render(request, 'Plantilla/plantillaCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")