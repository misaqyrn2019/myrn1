from django.shortcuts import render
from account.mixins import (
	FieldsMixin,
	FormValidMixin,
	AuthorAccessMixin,
	AuthorsAccessMixin,
	SuperUserAccessMixin,
    FacilitiesWelfareAccessMixin
)
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
    DetailView
)
from django.urls import reverse_lazy
from extensions.utils import jalali_converter
from django.shortcuts import render, get_object_or_404
from FacilitiesWelfare.models import *
from FacilitiesWelfare.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

class CashAssistanceList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = CashAssistance
    paginate_by = 10
    template_name = "FacilitiesWelfare/CashAssistance/CashAssistance_list.html"

    def get_queryset(self):
        return CashAssistance.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class CashAssistanceCreate(FacilitiesWelfareAccessMixin,DefineCachAssistance,CreateView):
    model = CashAssistance
    success_url = reverse_lazy('FacilitiesWelfare:homeCA')
    template_name = "FacilitiesWelfare/CashAssistance/CashAssistance-create-update.html"

    def get_queryset(self):
        return CashAssistance.objects.all()

class CashAssistanceUpdate(FacilitiesWelfareAccessMixin,DefineCachAssistance,UpdateView):
    model = CashAssistance
    success_url = reverse_lazy('FacilitiesWelfare:homeCA')
    template_name = "FacilitiesWelfare/CashAssistance/CashAssistance-create-update.html"

    def get_queryset(self):
        return CashAssistance.objects.all()

class CashAssistanceDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = CashAssistance
    success_url = reverse_lazy('FacilitiesWelfare:homeCA')
    template_name = "FacilitiesWelfare/CashAssistance/CashAssistance_confirm_delete.html"

class UserCashAssistance(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = CashAssistance
    paginate_by = 10
    template_name = "FacilitiesWelfare/CashAssistance/CashAssistance_list_User.html"

    def get_queryset(self):
        return CashAssistance.objects.filter(Q(IdUser=self.request.user) | Q(TypeAssistance="PU")).order_by("TypeAssistance")

    def get_object(self):
        return CashAssistance.objects.get(pk = self.request.user.pk)