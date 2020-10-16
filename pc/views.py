from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render

from .models import Pc
from .forms import PcForm

# Create your views here.
def index(request):
    pcs = Pc.objects.all()
    return render(request, 'pc/pc.html', { 'pcs': pcs })

def addPc(request):
    if request.method == 'POST':
        form = PcForm(request.POST)

        if form.is_valid():
            form.storage()
            return HttpResponse('Registrando pc')
        else:
            print(form.errors)
            return HttpResponse('formulario invalido <br/>' + str(form.errors))

    else:
        return redirect('/pc/')    