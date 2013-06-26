class SearchMixin(object):
	buscar = ''

	def get_queryset(self):
		queryset = super(SearchMixin, self).get_queryset()

		q = self.request.GET.get("q")
		if q:
			busqueda = self.buscar+'__icontains'
			return queryset.filter(**{busqueda:q})

		return queryset