from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_emprestimos, name='lista_emprestimos'),
    path('adicionar/', views.adicionar_emprestimo, name='adicionar_emprestimo'),
    path('emprestimos_json',views.emprestimos_json, name='emprestimos_json')
]
