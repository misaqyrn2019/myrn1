from django.shortcuts import render
from account.mixins import (
	FieldsMixin,
	FormValidMixin,
	AuthorAccessMixin,
	AuthorsAccessMixin,
	SuperUserAccessMixin,
    FacilitiesWelfareAccessMixin,
)
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
    DetailView
)
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from FacilitiesWelfare.models import *
from FacilitiesWelfare.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

class RelativesDeathServicesList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = RelativesDeathServices
    paginate_by = 10
    template_name = "FacilitiesWelfare/RelativesDeathServices/RelativesDeathServices_list.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return RelativesDeathServices.objects.all()
        elif self.request.User.is_FacilitiesWelfare:
            return RelativesDeathServices.objects.filter(author=self.request.user)

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class RelativesDeathServicesCreate(FacilitiesWelfareAccessMixin,DefineRelativesDeathServices,CreateView):
    model = RelativesDeathServices
    success_url = reverse_lazy('FacilitiesWelfare:homeRDS')
    template_name = "FacilitiesWelfare/RelativesDeathServices/RelativesDeathServices-create-update.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return RelativesDeathServices.objects.all()
        else:
            return RelativesDeathServices.objects.filter(author=self.request.user)

class RelativesDeathServicesUpdate(FacilitiesWelfareAccessMixin,DefineRelativesDeathServices,UpdateView):
    model = RelativesDeathServices
    success_url = reverse_lazy('FacilitiesWelfare:homeRDS')
    template_name = "FacilitiesWelfare/RelativesDeathServices/RelativesDeathServices-create-update.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return RelativesDeathServices.objects.all()
        else:
            return RelativesDeathServices.objects.filter(author=self.request.user)

class RelativesDeathServicesDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = RelativesDeathServices
    success_url = reverse_lazy('FacilitiesWelfare:homeRDS')
    template_name = "FacilitiesWelfare/RelativesDeathServices/RelativesDeathServices_confirm_delete.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return RelativesDeathServices.objects.all()
        elif self.request.user.is_storekeeper:
            return RelativesDeathServices.objects.filter(author=self.request.user)

class UserRelativesDeathServices(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = RelativesDeathServices
    paginate_by = 10
    template_name = "FacilitiesWelfare/RelativesDeathServices/RelativesDeathServices_list_User.html"

    def get_queryset(self):
        return RelativesDeathServices.objects.filter(IdUser=self.request.user)

    def get_object(self):
        return RelativesDeathServices.objects.get(pk = self.request.user.pk)