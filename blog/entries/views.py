#Vistas genericas de Django
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DetailView
#Mixins de https://github.com/brack3t/django-braces para reutilizar
from braces.views import LoginRequiredMixin

from core.views import SearchMixin

from .models import Entry
from .forms import EntryForm

class EntryActionMixin(object):

	@property
	def action(self):
		msg = "{0} is missing action.".format(self.__class__)
		raise NotImplementedError(msg)

	def form_valid(self, form):
		msg = "Entry {0}!".format(self.action)
		messages.info(self.request, msg)
		return super(EntryActionMixin, self).form_valid(form)

class EntryListView(SearchMixin, ListView):
	model = Entry
	buscar = 'slug'
	template_name = 'entries/entry_list.html'

class EntryCreateView(LoginRequiredMixin, EntryActionMixin, CreateView):
	model = Entry

	login_url = '/admin/'

	action = "created"
	template_name = 'entries/entry_create.html'

	form_class = EntryForm

class EntryUpdateView(EntryActionMixin, UpdateView):
	model = Entry

	action = 'updated'
	template_name = 'entries/entry_update.html'

	form_class = EntryForm

class EntryDetailView(DetailView):
	model = Entry

