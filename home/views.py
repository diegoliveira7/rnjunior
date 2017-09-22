from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib import messages

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
        context['NoticiasModel'] = Noticias.objects.all()
        context['ParceirosModel'] = Parceiros.objects.all()
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
        return render(request, self.template_name, context)


class HomeViewTeste(TemplateView):

    template_name = 'index.html'

    '''def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form_rodape'] = EnviarEmailRodape(self.request.POST or None)
        context['form_newsletter'] = NewsletterModelForm(self.request.POST or None)
        context['NoticiasModel'] = Noticias.objects.all()
        context['ParceirosModel'] = Parceiros.objects.all()
        context['AreaModel'] = AreaModel.objects.all()
        context['SetorModel'] = SetorModel.objects.all()
        context['EmpresaModel'] = EmpresaModel.objects.all()
        context['DiretorModel'] = Diretor.objects.all()
        context['AssessoresModel'] = Assessores.objects.all()
        return render(request, 'index.html', context)'''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_rodape'] = EnviarEmailRodape(self.request.POST or None)
        context['form_newsletter'] = NewsletterModelForm(self.request.POST or None)
        context['NoticiasModel'] = Noticias.objects.all()
        context['ParceirosModel'] = Parceiros.objects.all()
        context['AreaModel'] = AreaModel.objects.all()
        context['SetorModel'] = SetorModel.objects.all()
        context['EmpresaModel'] = EmpresaModel.objects.all()
        context['DiretorModel'] = Diretor.objects.all()
        context['AssessoresModel'] = Assessores.objects.all()
        return context


class NewsletterForm(FormView):

    form_class = NewsletterModelForm
    template_name = 'nano.html'
    success_url = "/"

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        form_newsletter = self.form_class(request.POST)
        form_rodape = EnviarEmailRodape()
        if form_newsletter.is_valid():
            form_newsletter.save()
            return render(request, 'index.html')
        else:
            return redirect('/')