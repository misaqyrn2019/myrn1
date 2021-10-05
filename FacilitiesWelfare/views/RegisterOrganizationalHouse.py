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

class RegisterOrganizationalHouseList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = RegisterOrganizationalHouse
    paginate_by = 10
    template_name = "FacilitiesWelfare/OrganizationalHouse/RegisterOrganizationalHouse_list.html"

    def get_queryset(self):
        return RegisterOrganizationalHouse.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(RegisterOrganizationalHouse, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class RegisterOrganizationalHouseCreate(FacilitiesWelfareAccessMixin,DefineRegisterOrganizationalHouse,CreateView):
    model = RegisterOrganizationalHouse
    success_url = reverse_lazy('FacilitiesWelfare:homeROH')
    template_name = "FacilitiesWelfare/OrganizationalHouse/RegisterOrganizationalHouse-create-update.html"

class RegisterOrganizationalHouseUpdate(FacilitiesWelfareAccessMixin,DefineRegisterOrganizationalHouse,UpdateView):
    model = RegisterOrganizationalHouse
    success_url = reverse_lazy('FacilitiesWelfare:homeROH')
    template_name = "FacilitiesWelfare/OrganizationalHouse/RegisterOrganizationalHouse-create-update.html"

class RegisterOrganizationalHouseDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = RegisterOrganizationalHouse
    success_url = reverse_lazy('FacilitiesWelfare:homeROH')
    template_name = "FacilitiesWelfare/OrganizationalHouse/RegisterOrganizationalHouse_confirm_delete.html"