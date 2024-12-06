from django.shortcuts import render, HttpResponse
from galeria.forms import FormAdiciona
from galeria.funcoes import salva_imagens

# Create your views here.

def Home(request):
  dic = {}
  form_adiciona = FormAdiciona()

  if request.method == 'POST':
    form_adiciona = FormAdiciona(request.POST)
    if form_adiciona.is_valid():
      filtros = {}
      filtros['tags'] = form_adiciona.cleaned_data['tags']
      filtros['imagens'] = request.FILES.getlist('imagens')

      resultado = salva_imagens(filtros)

  dic['form_adiciona'] = form_adiciona

  return render(request, 'base.html', dic)
