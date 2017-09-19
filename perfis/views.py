from django.shortcuts import render
from perfis.models import Perfil

# Create your views here.
def index(request):
    return render(request, 'index.html')

def exibir(request,perfil_id):

    perfil = Perfil()

    if perfil_id == '1':
        perfil = Perfil('Paulo Henrique','ph@yopmail.com','1234567','home')

    if perfil_id == '2':
        perfil = Perfil('Dev','dev@yopmail.com','89123456','work')


    return render(request, 'perfil.html',{"perfil" : perfil})
