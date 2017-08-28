from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import EnviarEmailRodape, NewsletterModelForm


class HomeView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_rodape'] = EnviarEmailRodape()
        context['form_newsletter'] = NewsletterModelForm()
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get('send') == "Enviar_rodape":
            form = EnviarEmailRodape(request.POST)
            if form.is_valid():
                form.enviar_email()
        elif request.POST.get('send') == "Enviar_newsletter":
            form = NewsletterModelForm(request.POST)
            if form.is_valid():
                form.save()
        return render(request, self.template_name, self.get_context_data())