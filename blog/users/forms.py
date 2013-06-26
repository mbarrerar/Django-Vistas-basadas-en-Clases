from django import forms

from .models import User

class UserCreateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ("first_name", "last_name", "username", "email")

class UserUpdateForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(UserUpdateForm, self).__init__(*args, **kwargs)
		self.fields["phone"].required = True
		self.fields["direction"].required = True

	class Meta(UserCreateForm.Meta):
		fields = ("first_name", "last_name", "username", "email", "phone", "direction")