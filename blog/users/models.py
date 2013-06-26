from django.core.urlresolvers import reverse
from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	email = models.EmailField()
	phone = models.CharField(max_length=12, blank=True)
	direction = models.CharField(max_length=255, blank=True)

	def get_absolute_url(self):
		return reverse("user_detail", kwargs={"pk": self.pk})

	def __unicode__(self):
		return ('%s') % self.username