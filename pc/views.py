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
            #return HttpResponse('Registrando pc')
            return redirect('/pc/')
        else:
            print(form.errors)
            return HttpResponse('formulario invalido <br/>' + str(form.errors))

    else:
        return redirect('/pc/')    

def delPc(request, id):
    pc = Pc.objects.get(pk=id)
    pc.delete()
    #return HttpResponse('Eliminando pc ' + str(id))
    return redirect('/pc/')

def editPc(request, id=-1):
    if request.method == 'GET':
        pcs = Pc.objects.all()
        pcEdit = Pc.objects.get(pk=id)
        return render(request, 'pc/pc.html', { 'pcs': pcs, 'pcEdit': pcEdit })    
    elif request.method == 'POST':
        form = PcForm(request.POST)

        if form.is_valid():
            form.update()
            #return HttpResponse('Registrando pc')
            return redirect('/pc/')
        else:
            print(form.errors)
            return HttpResponse('formulario invalido <br/>' + str(form.errors))

