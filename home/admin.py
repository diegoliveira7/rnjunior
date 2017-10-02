from django.contrib import admin
from .models import *


admin.site.site_header = 'Site Administrativo da RNJunior'

class ClienteNewsletterAdmin(admin.ModelAdmin):

	list_display = ['nome', 'email']
	search_fields = ['nome', 'email']
	list_filter = ['nome']


class NoticiasAdmin(admin.ModelAdmin):

	search_fields = ['texto']
	exclude = ('modificado', 'data_orientation', 'data_slice_1', 
		'data_slice_2', 'data_slice_1_scale', 'data_slice_2_scale',
		)
	prepopulated_fields = {'slug': ('titulo',)}


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
admin.site.register(Inteiro)