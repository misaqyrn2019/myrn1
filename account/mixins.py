from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from blog.models import Article
from FacilitiesWelfare.models import *

class FieldsMixin():
	def dispatch(self, request, *args, **kwargs):
		self.fields = [
			"title", "slug", "category",
			"description", "thumbnail", "publish",
			"is_special", "status",
		]
		if request.user.is_superuser:
			self.fields.append("author")
		return super().dispatch(request, *args, **kwargs)

class FormValidMixin():
	def form_valid(self, form):
		if self.request.user.is_superuser:
			form.save()
		else:
			self.obj = form.save(commit=False)
			self.obj.author = self.request.user
			if not self.obj.status == 'i':
				self.obj.status = 'd'
		return super().form_valid(form)

class AuthorAccessMixin():
	def dispatch(self, request, pk, *args, **kwargs):
		article = get_object_or_404(Article, pk=pk)
		if article.author == request.user and article.status in ['b', 'd'] or\
		request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404("You can't see this page.")

class AuthorsAccessMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			if request.user.is_superuser or request.user.is_author:
				return super().dispatch(request, *args, **kwargs)
			else:
				return redirect("account:profile")
		else:
			return redirect("login")

class SuperUserAccessMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404("You can't see this page.")

class FacilitiesWelfareAccessMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_FacilitiesWelfare or request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404("You can't see this page.")

class StorekeeperUserAccessMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_storekeeper or request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404("You can't see this page.")

class FWAccessMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user == self.request.user:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404("You can't see this page.")


class AAMixin():
	def dispatch(self, request, *args, **kwargs):
		CIR = ConsumerItemsRegister.objects.filter(Q(IdUser=5)).count()
		if(CIR >= 1):
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404("You can't see this page.")