from django.views.generic import CreateView, UpdateView, DetailView, ListView

from core.views import SearchMixin
from .models import User
from .forms import UserCreateForm, UserUpdateForm

class UserListView(SearchMixin, ListView):

	model = User
	buscar = 'first_name'
	template_name = 'users/user_list.html'

class UserCreateView(CreateView):

	model = User
	template_name = 'users/user_create.html'
	form_class = UserCreateForm

class UserUpdateView(UpdateView):

	model = User
	template_name = 'users/user_update.html'
	form_class = UserUpdateForm

class UserDetailView(DetailView):

	model = User
	template_name = 'users/user_detail.html'