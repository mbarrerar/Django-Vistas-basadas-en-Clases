from django.core.urlresolvers import reverse
from django.db import models

from core.models import EntryTitleAbstractModel

class Entry(EntryTitleAbstractModel):
	'''
	La clase entrada solo cuenta con un titulo, un slug y una 
	caja de texto con WISIG para escribir las entradas.
	'''
	content = models.TextField()
	slug = models.SlugField()
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse("entry_detail", kwargs={'pk':self.pk})

	def __unicode__(self):
		return ('%s') % self.title