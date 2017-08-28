from django import forms
from django.core.mail import send_mail
from django.conf import settings

from .models import ClienteNewsletter


class EnviarEmailRodape(forms.Form):

    nome = forms.CharField(label="Nome", max_length=100, widget=forms.TextInput({'required': 'required'}))
    email = forms.CharField(label="E-mail", widget=forms.EmailInput({'required': 'required'}))
    texto = forms.CharField(label="Texto", widget=forms.Textarea({'required': 'required'}))

    def enviar_email(self):
        nome_cliente = self.cleaned_data['nome']
        email_cliente = self.cleaned_data['email']
        mensagem = "Olá, \nNovo email de contato no site\nContato: " + nome_cliente \
            + "\nEmail do usuario: " + email_cliente + "\nMensagem: " + self.cleaned_data['texto']
        send_mail(
            nome_cliente,
            mensagem,
            settings.DEFAULT_FROM_EMAIL,
            ['to@example.com'],
            fail_silently=False,
        )


class NewsletterModelForm(forms.ModelForm):

    class Meta:
        model = ClienteNewsletter
        fields = ['nome', 'email']
