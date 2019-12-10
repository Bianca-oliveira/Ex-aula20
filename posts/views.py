from django.shortcuts import render

# Create your views here.
def home(request):
    nome = 'Bianca'
    lista = ['Bianca, Caroline, Bruna, Hugo']
    contexto = {
        'nome': nome
    }
    return render(request, 'home.html', contexto)
def post(request):
    return render(request, 'post.html')

def cadastro(request):
    return render(request, 'cadastro.html')
