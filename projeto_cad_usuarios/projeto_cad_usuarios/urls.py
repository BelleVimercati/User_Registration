
from django.urls import path
from app_cad_usuarios import views

#criação de rotas
urlpatterns = [
    #rota, view responsável, nome de referencia
    path('', views.home,name='home' ), #vazio pois é pagina inicial

    path('usuarios/', views.usuarios, name='listagem_usuarios'), #precisamos usar o mesmo nome que colocamos no html referenciando a página no form -> action 
]
