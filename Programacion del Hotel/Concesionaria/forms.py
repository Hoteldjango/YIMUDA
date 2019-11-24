from django import forms
from . models import Habitacion , Clases , Opinion , Promocion , Reserva , Contacto
from bootstrap_datepicker_plus import DatePickerInput



class HabitacionForm(forms.ModelForm):
	class Meta:
		model = Habitacion
		fields = ('numero_habitacion','imagen','precio','capacidad','clase','informacion','estado')


class ClaseForm(forms.ModelForm):
	class Meta:
		model = Clases
		fields = ('tipos','precios')

class OpinionForm(forms.ModelForm):
	class Meta:
		model = Opinion
		fields = ('descripcion','nombre','apellido','email')

class ContactoForm(forms.ModelForm):
	class Meta:
		model = Contacto
		fields = ('descripcion','nombre','apellido','email')

class PromocionForm(forms.ModelForm):
	class Meta:
		model = Promocion
		fields = ('datos','id_habitacion','vigencia')


class ReservaForm(forms.ModelForm):
	class Meta:
		model = Reserva
		fields = ('nombre','apellido','clase','consulta','fecha_inicio','fecha_fin')
		widgets = {
            'fecha_inicio': DatePickerInput(format='%Y-%m-%d'),
            'fecha_fin': DatePickerInput(format='%Y-%m-%d'), 
        }