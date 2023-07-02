from django.urls import path
from . import views 

app_name = 'smartparking'  # Reemplaza "nombre_de_tu_aplicacion" con el nombre real de tu aplicación

urlpatterns = [
    path('estacionamiento/', views.lista_estacionamientos, name='estacionamientos'),
    path('estados_estacionamiento/<int:estacionamiento_id>/', views.estados_estacionamiento, name='estados_estacionamiento'),
    path('empresas/', views.empresas, name='empresas'),

    path('login/', views.login_view, name="login"),
    
    path('about/',views.about,name="about"),
    path('logout/', views.logout_view, name="logout"),

    path('',views.home, name='home')
]