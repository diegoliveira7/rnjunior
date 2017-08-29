from django.db import models
from django.conf import settings
from django.core.mail import send_mail


#Modelo responsável por salvar o pessoal no Newsletter
class ClienteNewsletter(models.Model):

    nome = models.CharField("Nome do cliente", max_length=100)
    email = models.EmailField("E-mail do cliente")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletter"


#Cadastra as notícias e joga no SlideShow
class Noticias(models.Model):

    texto = models.CharField("Texto", max_length=100)
    imagem = models.ImageField("Imagem", upload_to="%y/%m/%d")
    texto_teste = models.CharField(max_length=100, blank=True)

    #Sobrescrevi o método save padrão do modelo para que
    #quando uma nova instância fosse criada e salva,
    #fosse enviado um email a todos os inscritos no Newsletter
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
        """
        data-orientation="horizontal" data-slice1-rotation="-25" data-slice2-rotation="-25" 
        data-slice1-scale="2" data-slice2-scale="2"
        """
        num = Inteiro.objects.get(id=1)
        if num.num == 1:
            self.texto_teste = "horizontal"
        elif num.num == 2:
            pass
        else:
            pass
        super().save(*args, **kwargs)

    def __str__(self):
        return self.texto[:100]

    class Meta:
        verbose_name = "Notícia"


#Modelo para salvar os parceiros
class Parceiros(models.Model):

    foto = models.ImageField("Imagem", upload_to="%y/%m/%d")
    titulo = models.CharField("Título", max_length=100)
    texto = models.TextField("Texto")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Parceiro"


class Inteiro(models.Model):

    num = models.PositiveSmallIntegerField()
