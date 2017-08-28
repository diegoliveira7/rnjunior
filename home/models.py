from django.db import models
from django.conf import settings
from django.core.mail import send_mail


class ClienteNewsletter(models.Model):

	nome = models.CharField("Nome do cliente", max_length=100)
	email = models.EmailField("E-mail do cliente")

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = "Newsletter"
		verbose_name_plural = "Newsletter"

class Noticias(models.Model):

	texto = models.CharField("Texto", max_length=100)

	def save(self, *args, **kwargs):
		listaDosEmails = []
		for i in ClienteNewsletter.objects.all():
			listaDosEmails.append(i.email)
		send_mail(
            "Nome do camarada",
            self.texto,
            settings.DEFAULT_FROM_EMAIL,
            listaDosEmails,
            fail_silently=False,
        )
		super().save(*args, **kwargs)

	class Meta:
		verbose_name = "Notícia"

	def __str__(self):
		return self.texto[:100]