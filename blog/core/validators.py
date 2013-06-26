from django.core.exceptions import ValidationError

def validate_entry(value):
	'''La entrada deberia comenzar con mayuscula la primera letra'''

	if not value.startswith(u'A'):
		msg = u"El titulo deberia empezar con A"
		raise ValidationError(msg)