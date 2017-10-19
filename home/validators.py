from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

	
def validador_de_data(data):
	if not(data <= timezone.now()):
		raise ValidationError(
			_("A data inserida não é válida"),
		)