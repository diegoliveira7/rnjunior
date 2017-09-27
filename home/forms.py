from django import forms
from django.core.mail import send_mail
from django.conf import settings

from .models import ClienteNewsletter


#Formulário criado para enviar os e-mails do rodapé
class EnviarEmailRodape(forms.Form):

    nome = forms.CharField(label="Nome", max_length=100, widget=forms.TextInput({'required': 'required', 'placeholder': 'Nome'}))
    email = forms.CharField(label="E-mail", widget=forms.EmailInput({'required': 'required', 'placeholder': 'Email'}))
    assunto = forms.CharField(label="Assunto", max_length=100, widget=forms.TextInput({'required': 'required', 'placeholder': 'Assunto'}))
    texto = forms.CharField(label="Texto", widget=forms.Textarea({'required': 'required', 'placeholder': 'Mensagem'}))

    def enviar_email(self):
        nome_cliente = self.cleaned_data['nome']
        email_cliente = self.cleaned_data['email']
        assunto_cliente = self.cleaned_data['assunto']
        mensagem = "Olá, \nNovo email de contato no site\nContato: " + nome_cliente \
            + "\nEmail do usuario: " + email_cliente + "\nAssunto: " + assunto_cliente + "\nMensagem: " + self.cleaned_data['texto']
        send_mail(
            nome_cliente,
            mensagem,
            settings.DEFAULT_FROM_EMAIL,
            ['to@example.com'],
            fail_silently=False,
        )


#Formulário criado para salvar os clientes no newsletter
class NewsletterModelForm(forms.ModelForm):

    class Meta:
        model = ClienteNewsletter
        fields = ['nome', 'email']


class EnviarEmailModel(forms.Form):

    nome = forms.CharField(label="Nome", max_length=100, widget=forms.TextInput({'required': 'required', 'placeholder': 'Nome'}))
    email = forms.CharField(label="E-mail", widget=forms.EmailInput({'required': 'required', 'placeholder': 'Email'}))
    mensagem = forms.CharField(label="Assunto", max_length=100, widget=forms.Textarea({'required': 'required', 'placeholder': 'Mensagem'}))

    def enviar_email(self, email_empresa):
        nomeCliente = self.cleaned_data['nome']
        emailCliente = self.cleaned_data['email']
        mensagemCliente = self.cleaned_data['mensagem']
        send_mail(
            nomeCliente,
            mensagemCliente,
            settings.DEFAULT_FROM_EMAIL,
            [email_empresa],
            fail_silently=False
        )