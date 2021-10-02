from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from blog.models import Article

class StorekeeperUserAccessMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_storekeeper:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404("You can't see this page.")