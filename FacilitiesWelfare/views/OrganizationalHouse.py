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

class OrganizationalHouseList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = OrganizationalHouse
    paginate_by = 10
    template_name = "FacilitiesWelfare/OrganizationalHouse/OrganizationalHouse_list.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return OrganizationalHouse.objects.all()
        elif self.request.User.is_FacilitiesWelfare:
            return OrganizationalHouse.objects.filter(author=self.request.user)

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class OrganizationalHouseCreate(FacilitiesWelfareAccessMixin,DefineOrganizationalHouse,CreateView):
    model = OrganizationalHouse
    success_url = reverse_lazy('FacilitiesWelfare:homeOH')
    template_name = "FacilitiesWelfare/OrganizationalHouse/OrganizationalHouse-create-update.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return OrganizationalHouse.objects.all()
        else:
            return OrganizationalHouse.objects.filter(author=self.request.user)

class OrganizationalHouseUpdate(FacilitiesWelfareAccessMixin,DefineOrganizationalHouse,UpdateView):
    model = OrganizationalHouse
    success_url = reverse_lazy('FacilitiesWelfare:homeOH')
    template_name = "FacilitiesWelfare/OrganizationalHouse/OrganizationalHouse-create-update.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return OrganizationalHouse.objects.all()
        else:
            return OrganizationalHouse.objects.filter(author=self.request.user)

class OrganizationalHouseDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = OrganizationalHouse
    success_url = reverse_lazy('FacilitiesWelfare:homeOH')
    template_name = "FacilitiesWelfare/OrganizationalHouse/OrganizationalHouse_confirm_delete.html"


class UserOrganizationalHouseListAll(LoginRequiredMixin,ListView):
    model = OrganizationalHouse
    template_name = "FacilitiesWelfare/OrganizationalHouse/OrganizationalHouse_ListAll.html"

class OrganizationalHouseRegUser(LoginRequiredMixin,ListView):
    model = OrganizationalHouse
    template_name = "FacilitiesWelfare/OrganizationalHouse/OrganizationalHouse-Save.html"

    def get_queryset(self,**kwargs):
        pk=self.kwargs.get('pk')
        return pk

class OrganizationalHouseRegUser2(LoginRequiredMixin,DefineRegisterOrganizationalHouse,CreateView):
    model = RegisterOrganizationalHouse
    success_url = reverse_lazy('FacilitiesWelfare:OrganizationalHouse-LST-User')

class OrganizationalHouseListUser(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = RegisterOrganizationalHouse
    paginate_by = 10
    template_name = "FacilitiesWelfare/OrganizationalHouse/OrganizationalHouseUser.html"

    def get_queryset(self):
        return RegisterOrganizationalHouse.objects.filter(
            Q(IdUser=self.request.user.pk)
            )

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs