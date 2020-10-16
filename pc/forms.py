from django import forms
from .models import Pc
from datetime import datetime

class PcForm(forms.Form):
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
