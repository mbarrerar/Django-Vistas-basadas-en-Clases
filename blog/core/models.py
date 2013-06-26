from django.db import models

from .validators import validate_entry

class EntryTitleAbstractModel(models.Model):
	title = models.CharField(max_length=255, validators=[validate_entry])

	class Meta:
		abstract = True
