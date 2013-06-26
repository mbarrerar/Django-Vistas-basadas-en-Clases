from django import forms

from core.validators import validate_entry
from .models import Entry

class EntryForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(EntryForm, self).__init__(*args, **kwargs)
		self.fields["title"].validators.append(validate_entry)
		self.fields["slug"].validators.append(validate_entry)

	class Meta:
		model = Entry