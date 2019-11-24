
from django.contrib import admin
#from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from Concesionaria import views

urlpatterns = [
	path('index/', views.index, name='index'),
	path('base/', views.base, name='inicio'),
	path('', views.index_usuario, name='index_usuario'),


	
	path('restaurante/', views.restaurante, name='restaurante'),
	path('contacto/', views.contacto, name='contacto'),
	path('exito/', views.exito, name='exito'),


	path('habitaciones_usuarios',views.habitaciones_usuarios, name='habitaciones_usuarios'),
	

	path('reservas_usuarios',views.reservas_usuarios, name='reservas_usuarios'),


	path('contacto_nuevo/', views.contacto_nuevo, name='contacto_nuevo'),
	path('contacto_borrar/<int:pk>/', views.contacto_borrar, name='contacto_borrar'),
	path('contacto_modificar/<int:pk>/', views.contacto_modificar, name='contacto_modificar'),
	path('contacto_ver/', views.contacto_ver , name='contacto_ver'),

	path('opiniones_usuarios/', views.opiniones_usuarios, name='opiniones_usuarios'),

	path('opinion_nuevo/', views.opinion_nuevo, name='opinion_nuevo'),
	path('opinion_borrar/<int:pk>/', views.opinion_borrar, name='opinion_borrar'),
	path('opinion_modificar/<int:pk>/', views.opinion_modificar, name='opinion_modificar'),
	path('opinion_ver/', views.opinion_ver , name='opinion_ver'),


	path('habitacion_nuevo/', views.habitacion_nuevo, name='habitacion_nuevo'),
	path('habitacion_borrar/<int:pk>/', views.habitacion_borrar, name='habitacion_borrar'),
	path('habitacion_modificar/<int:pk>/', views.habitacion_modificar, name='habitacion_modificar'),
	path('habitacion_ver/', views.habitacion_ver , name='habitacion_ver'),

	path('clase_nuevo/', views.clase_nuevo, name='clase_nuevo'),
	path('clase_borrar/<int:pk>/', views.clase_borrar, name='clase_borrar'),
	path('clase_modificar/<int:pk>/', views.clase_modificar, name='clase_modificar'),
	path('clase_ver/', views.clase_ver , name='clase_ver'),

	path('promocion_nuevo/', views.promocion_nuevo, name='promocion_nuevo'),
	path('promocion_borrar/<int:pk>/', views.promocion_borrar, name='promocion_borrar'),
	path('promocion_modificar/<int:pk>/', views.promocion_modificar, name='promocion_modificar'),
	path('promocion_ver/', views.promocion_ver , name='promocion_ver'),
	
	path('reserva_nuevo/', views.reserva_nuevo, name='reserva_nuevo'),
	path('reserva_borrar/<int:pk>/', views.reserva_borrar, name='reserva_borrar'),
	path('reserva_modificar/<int:pk>/', views.reserva_modificar, name='reserva_modificar'),
	path('reserva_ver/', views.reserva_ver , name='reserva_ver'),

] 

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
