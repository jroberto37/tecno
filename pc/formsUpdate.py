from django import forms
from .models import Pc
from datetime import datetime

class PcFormUpdate(forms.Form):
    idPc = forms.IntegerField()
    modelo = forms.CharField(max_length=10)
    fecha = forms.DateField()


    def storage(self):
        modelo_ = self.cleaned_data.get('modelo')
        fecha_ = self.cleaned_data.get('fecha')
        t = datetime.now()
        hora = t.strftime("%H:%M:%S")
        type(hora)
        #fecha_ = fecha_ + ' ' + hora

        nuevoPc = Pc (
            modelo = modelo_, 
            fecha = fecha_
            )

        nuevoPc.save()

    def update(self):
        id_ = self.cleaned_data.get('idPc')
        modelo_ = self.cleaned_data.get('modelo')
        fecha_ = self.cleaned_data.get('fecha')
        print('Id a actualizar ->',id_)
        oldPc = Pc.objects.get(id=id_)
        oldPc.modelo = modelo_
        oldPc.fecha = fecha_
        oldPc.save()        
