from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView

from .forms import EnviarEmailRodape, NewsletterModelForm, EnviarEmailModel
from .models import Noticias, Parceiros, AreaModel, SetorModel, EmpresaModel, \
                    Diretor, Assessores, Eventos

#View mestra que recebe todos os valores de contexto e
#valida os formulários
class HomeView(TemplateView):

    template_name = 'index.html'

    #Pega os  valores e joga no template como variáveis a serem usadas
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_rodape'] = EnviarEmailRodape()
        context['form_newsletter'] = NewsletterModelForm()
        context['NoticiasModel'] = Noticias.objects.all()
        context['ParceirosModel'] = Parceiros.objects.all()
        context['AreaModel'] = AreaModel.objects.all()
        context['SetorModel'] = SetorModel.objects.all()
        context['EmpresaModel'] = EmpresaModel.objects.all()
        context['DiretorModel'] = Diretor.objects.all()
        context['AssessoresModel'] = Assessores.objects.all()
        context['form_enviar_email_model'] = EnviarEmailModel()
        context['CrieSuaEJModel'] = Eventos.objects.all()
        return context

    #Quando tem um método "post" a view processa o pedido
    #e checa qual dos forms que veio o pedido e faz o
    #devido procedimento
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        #Pergunta se o pedido foi do formulário de envio de email
        if request.POST.get('form_rodape') == "Enviar":
            form = EnviarEmailRodape(request.POST)
            context['form_newsletter'] = NewsletterModelForm()
            context['form_rodape'] = form
            if form.is_valid():
                form.enviar_email()
                context['form_rodape'] = EnviarEmailRodape()
                context['success_form_rodape'] = True
        #Pergunta se o pedido foi do formulário de newsletter
        elif request.POST.get('form_newsletter') == "Enviar_newsletter":
            form = NewsletterModelForm(request.POST)
            context['form_rodape'] = EnviarEmailRodape()
            context['form_newsletter'] = form
            if form.is_valid():
                form.save()
                context['form_newsletter'] = NewsletterModelForm()
                context['success_form_newsletter'] = True
        #Pergunta se o pedido foi das empresas
        elif request.POST.get('form_modal')[0:12] == 'Enviar_Modal':
            form = EnviarEmailModel(request.POST)
            if form.is_valid():
                nomeEmpresa = request.POST.get('form_modal')[12:]
                Empresa = EmpresaModel.objects.get(nome_empresa=nomeEmpresa)
                form.enviar_email(Empresa.email_empresa)
        return render(request, self.template_name, context)


class NoticiaView(DetailView):

    model = Noticias
    template_name = 'noticia.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Noticias, slug=self.kwargs['slug'])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticia'] = self.get_object()
        return context