from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import EnviarEmailRodape, NewsletterModelForm
from .models import Noticias, Parceiros, AreaModel, SetorModel, EmpresaModel, \
                    Diretor, Assessores

#View mestra que recebe todos os valores de contexto e
#valida os formulários
class HomeView(TemplateView):

    template_name = 'index.html'

    #Pega os  valores e joga no template como variáveis a serem usadas
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_rodape'] = EnviarEmailRodape()
        context['form_newsletter'] = NewsletterModelForm()
        context['noticias'] = Noticias.objects.all()
        context['parceiros'] = Parceiros.objects.all()
        context['AreaModel'] = AreaModel.objects.all()
        context['SetorModel'] = SetorModel.objects.all()
        context['EmpresaModel'] = EmpresaModel.objects.all()
        context['DiretorModel'] = Diretor.objects.all()
        context['AssessoresModel'] = Assessores.objects.all()
        return context

    #Quando tem um método "post" a view processa o pedido
    #e checa qual dos forms que veio o pedido e faz o
    #devido procedimento
    def post(self, request, *args, **kwargs):
        #Pergunta se o pedido foi do formulário de envio de email
        if request.POST.get('form_rodape') == "Enviar":
            form = EnviarEmailRodape(request.POST)
            if form.is_valid():
                form.enviar_email()
        #Pergunta se o pedido foi do formulário de newsletter
        elif request.POST.get('form_newsletter') == "Enviar_newsletter":
            form = NewsletterModelForm(request.POST)
            if form.is_valid():
                form.save()
        return render(request, self.template_name, self.get_context_data())