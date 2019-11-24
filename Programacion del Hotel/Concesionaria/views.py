from django.shortcuts import render,redirect, get_object_or_404
from .models import Habitacion , Clases , Opinion , Promocion , Reserva , Contacto
from .forms import HabitacionForm , ClaseForm , OpinionForm , PromocionForm , ReservaForm, ContactoForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#Habitacion
@login_required(login_url='/accout/login')
def index(request):
    return render(request, 'Concesionaria/index.html', {})

@login_required(login_url='/accout/login')
def base(request):
    return render(request, 'Concesionaria/base.html', {})

##########################################################################################################

@login_required(login_url='/accout/login')
def habitacion_ver(request):
	habitaciones = Habitacion.objects.all()
	return render(request, 'Concesionaria/ver_habitacion.html', {'habitaciones':habitaciones})

@login_required(login_url='/accout/login')
def habitacion_nuevo(request):
	if request.method == "POST":
		form = HabitacionForm(request.POST)  
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('habitacion_ver')
	else:
		agregar_form = HabitacionForm()
		return render(request, 'Concesionaria/agregar_habitacion.html', {'agregar_form': agregar_form})

@login_required(login_url='/accout/login')
def habitacion_borrar(request , pk):
	habitacion = get_object_or_404(Habitacion, pk = pk)
	habitacion.delete()
	return redirect('habitacion_ver')

@login_required(login_url='/accout/login')
def habitacion_modificar(request , pk):
	habitacion = get_object_or_404(Habitacion, pk = pk)
	if request.method == 'POST':
		form = HabitacionForm(request.POST, instance=habitacion)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return redirect('habitacion_ver')
	else:
		form = HabitacionForm(instance=habitacion)
	return render(request,'Concesionaria/modificar_habitacion.html', {'form':form})


##########################################################################################################
def contacto(request):
	if request.method == "POST":
		form = ContactoForm(request.POST)  
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('exito')
	else:
		agregar_form = OpinionForm()
		return render(request, 'usuarios/contacto.html', {'agregar_form': agregar_form})
def restaurante(request):
    return render(request, 'usuarios/restaurante.html', {})    

@login_required(login_url='/accout/login')
def opiniones_usuarios(request):
	if request.method == "POST":
		form = OpinionForm(request.POST)  
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('opiniones_usuarios')
	else:
		agregar_form = OpinionForm()
		return render(request, 'usuarios/opiniones_usuarios.html', {'agregar_form': agregar_form})


def index_usuario(request):
    return render(request, 'usuarios/index_usuario.html', {})
    

def habitaciones_usuarios(request):
	habitaciones_usuarios = Habitacion.objects.all()
	return render(request, 'usuarios/habitaciones_usuarios.html', {'habitaciones_usuarios':habitaciones_usuarios})

@login_required(login_url='/accout/login')
def exito(request):
    return render(request, 'usuarios/exito.html', {})
# @login_required(login_url='/accout/login')
# def reservas_usuarios(request):
# 	if request.method == "POST":
# 		print (request.POST)
# 		# si pertenece al nuevo modelo -- lo manda a otra vista donde diga que esta ocupada la habiacion
# 		form = ReservaForm(request.POST)
# 		if form.is_valid():
# 			reserva = form.save(commit=False)

# 			habitacion = Habitacion.objects.get(clase__tipos=reserva.clase)
# 			request.POST['fecha_inicio']
# 			reserva.habitacion = habitacion[1]
			
# 			reserva.save()
# 			# guardar en el otro modelo , fecha, reser
# 			return redirect('exito')
# 	else:
# 		agregar_form = ReservaForm()
# 		return render(request, 'usuarios/reservas_usuarios.html', {'agregar_form': agregar_form})

@login_required(login_url='/accout/login')
def reservas_usuarios(request):
	if request.method == "POST":
		print (request.POST)
		form = ReservaForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('exito')
	else:
		agregar_form = ReservaForm()
		return render(request, 'usuarios/reservas_usuarios.html', {'agregar_form': agregar_form})



##########################################################################################################

@login_required(login_url='/accout/login')
def clase_ver(request):
	clases = Clases.objects.all()
	return render(request, 'Concesionaria/ver_clase.html', {'clases':clases})

@login_required(login_url='/accout/login')
def clase_nuevo(request):
	if request.method == "POST":
		form = ClaseForm(request.POST)  
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('clase_ver')
	else:
		agregar_form = ClaseForm()
		return render(request, 'Concesionaria/agregar_clase.html', {'agregar_form': agregar_form})

@login_required(login_url='/accout/login')
def clase_borrar(request , pk):
	clase = get_object_or_404(Clases, pk = pk)
	clase.delete()
	return redirect('clase_ver')

@login_required(login_url='/accout/login')
def clase_modificar(request , pk):
	clase = get_object_or_404(Clases, pk = pk)
	if request.method == 'POST':
		form = ClaseForm(request.POST, instance=clase)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return redirect('clase_ver')
	else:
		form = ClaseForm(instance=clase)
	return render(request,'Concesionaria/modificar_clase.html', {'form':form})

##########################################################################################################

@login_required(login_url='/accout/login')
def opinion_ver(request):
	opiniones = Opinion.objects.all()
	return render(request, 'Concesionaria/ver_opinion.html', {'opiniones':opiniones})

@login_required(login_url='/accout/login')
def opinion_nuevo(request):
	if request.method == "POST":
		form = OpinionForm(request.POST)  
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('opinion_ver')
	else:
		agregar_form = OpinionForm()
		return render(request, 'Concesionaria/agregar_opinion.html', {'agregar_form': agregar_form})

@login_required(login_url='/accout/login')
def opinion_borrar(request , pk):
	opinion = get_object_or_404(Opinion, pk = pk)
	opinion.delete()
	return redirect('opinion_ver')

@login_required(login_url='/accout/login')
def opinion_modificar(request , pk):
	opinion = get_object_or_404(Opinion, pk = pk)
	if request.method == 'POST':
		form = OpinionForm(request.POST, instance=opinion)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return redirect('opinion_ver')
	else:
		form = OpinionForm(instance=opinion)
	return render(request,'Concesionaria/modificar_opinion.html', {'form':form})

# ##########################################################################################################

@login_required(login_url='/accout/login')
def contacto_ver(request):
	contacto = Contacto.objects.all()
	return render(request, 'Concesionaria/ver_contacto.html', {'contacto':contacto})

@login_required(login_url='/accout/login')
def contacto_nuevo(request):
	if request.method == "POST":
		form = ContactoForm(request.POST)  
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('contacto_ver')
	else:
		agregar_form = ContactoForm()
		return render(request, 'Concesionaria/agregar_contacto.html', {'agregar_form': agregar_form})

@login_required(login_url='/accout/login')
def contacto_borrar(request , pk):
	contacto = get_object_or_404(Contacto, pk = pk)
	contacto.delete()
	return redirect('contacto_ver')

@login_required(login_url='/accout/login')
def contacto_modificar(request , pk):
	contacto = get_object_or_404(Contacto, pk = pk)
	if request.method == 'POST':
		form = ContactoForm(request.POST, instance=contacto)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return redirect('contacto_ver')
	else:
		form = ContactoForm(instance=contacto)
	return render(request,'Concesionaria/modificar_contacto.html', {'form':form})

##########################################################################################################

@login_required(login_url='/accout/login')
def promocion_ver(request):
	promociones = Promocion.objects.all()
	return render(request, 'Concesionaria/ver_promocion.html', {'promociones':promociones})

@login_required(login_url='/accout/login')
def promocion_nuevo(request):
	if request.method == "POST":
		form = PromocionForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('promocion_ver')
	else:
		agregar_form = PromocionForm()
		return render(request, 'Concesionaria/agregar_promocion.html', {'agregar_form': agregar_form})

@login_required(login_url='/accout/login')
def promocion_borrar(request , pk):
	promocion = get_object_or_404(Promocion, pk = pk)
	promocion.delete()
	return redirect('promocion_ver')

@login_required(login_url='/accout/login')
def promocion_modificar(request , pk):
	promocion = get_object_or_404(Promocion, pk = pk)
	if request.method == 'POST':
		form = PromocionForm(request.POST, instance=promocion)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return redirect('promocion_ver')
	else:
		form = PromocionForm(instance=promocion)
	return render(request,'Concesionaria/modificar_promocion.html', {'form':form})

##########################################################################################################

@login_required(login_url='/accout/login')
def reserva_ver(request):
	reservas = Reserva.objects.all()
	return render(request, 'Concesionaria/ver_reserva.html', {'reservas':reservas})

@login_required(login_url='/accout/login')
def reserva_nuevo(request):
	if request.method == "POST":
		print (request.POST)
		form = ReservaForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			request.POST['fecha_inicio']
			post.save()
			return redirect('reserva_ver')
	else:
		agregar_form = ReservaForm()
		return render(request, 'Concesionaria/agregar_reserva.html', {'agregar_form': agregar_form})

@login_required(login_url='/accout/login')
def reserva_borrar(request , pk):
	reserva = get_object_or_404(Reserva, pk = pk)
	reserva.delete()
	return redirect('reserva_ver')

@login_required(login_url='/accout/login')
def reserva_modificar(request , pk):
	reserva = get_object_or_404(Reserva, pk = pk)
	if request.method == 'POST':
		form = ReservaForm(request.POST, instance=reserva)
		if form.is_valid():
			form = form.save(commit=False)
			request.POST['fecha_inicio']
			form.save()
			return redirect('reserva_ver')
	else:
		modificar_form = ReservaForm(instance=reserva)
	return render(request,'Concesionaria/modificar_reserva.html', {'modificar_form':modificar_form})

