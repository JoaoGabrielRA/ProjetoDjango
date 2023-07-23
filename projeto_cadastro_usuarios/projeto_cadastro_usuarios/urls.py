from django.urls import path
from app_cadastro_usuarios import views

urlpatterns = [
   path('',views.home,name='home'),
   path('usuarios/', views.usuarios,name='listagem_usuarios'),
   path('delete/<int:id_usuario>', views.delete , name='delete'),
]
