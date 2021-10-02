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

class AssistanceList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = Assistance
    paginate_by = 10
    template_name = "FacilitiesWelfare/Assistance/Assistance_list.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return Assistance.objects.all()
        elif self.request.User.is_FacilitiesWelfare:
            return Assistance.objects.filter(author=self.request.user)

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class AssistanceCreate(FacilitiesWelfareAccessMixin,DefineAssistance,CreateView):
    model = Assistance
    success_url = reverse_lazy('FacilitiesWelfare:homeASis')
    template_name = "FacilitiesWelfare/Assistance/Assistance-create-update.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return Assistance.objects.all()
        else:
            return Assistance.objects.filter(author=self.request.user)

class AssistanceUpdate(FacilitiesWelfareAccessMixin,DefineAssistance,UpdateView):
    model = Assistance
    success_url = reverse_lazy('FacilitiesWelfare:homeASis')
    template_name = "FacilitiesWelfare/Assistance/Assistance-create-update.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return Assistance.objects.all()
        else:
            return Assistance.objects.filter(author=self.request.user)

class AssistanceDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = Assistance
    success_url = reverse_lazy('FacilitiesWelfare:homeASis')
    template_name = "FacilitiesWelfare/Assistance/Assistance_confirm_delete.html"