from django.contrib import admin
from .models import *


admin.site.site_header = 'Site Administrativo da RNJunior'

class ClienteNewsletterAdmin(admin.ModelAdmin):

	list_display = ['nome', 'email']
	search_fields = ['nome', 'email']
	list_filter = ['nome']


class NoticiasAdmin(admin.ModelAdmin):

	search_fields = ['texto']


class ParceirosAdmin(admin.ModelAdmin):

	search_fields = ['titulo', 'texto']


admin.site.register(ClienteNewsletter, ClienteNewsletterAdmin)
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Parceiros, ParceirosAdmin)
admin.site.register(AreaModel)
admin.site.register(SetorModel)
admin.site.register(EmpresaModel)
admin.site.register(Diretor)
admin.site.register(Assessores)