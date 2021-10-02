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

class FreeHelpList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = FreeHelp
    paginate_by = 10
    template_name = "FacilitiesWelfare/FreeHelp/FreeHelp_list.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return FreeHelp.objects.all()
        elif self.request.User.is_FacilitiesWelfare:
            return FreeHelp.objects.filter(author=self.request.user)

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class FreeHelpCreate(FacilitiesWelfareAccessMixin,DefineFreeHelp,CreateView):
    model = FreeHelp
    success_url = reverse_lazy('FacilitiesWelfare:homeFH')
    template_name = "FacilitiesWelfare/FreeHelp/FreeHelp-create-update.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return FreeHelp.objects.all()
        else:
            return FreeHelp.objects.filter(author=self.request.user)

class FreeHelpUpdate(FacilitiesWelfareAccessMixin,DefineFreeHelp,UpdateView):
    model = FreeHelp
    success_url = reverse_lazy('FacilitiesWelfare:homeFH')
    template_name = "FacilitiesWelfare/FreeHelp/FreeHelp-create-update.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return FreeHelp.objects.all()
        else:
            return FreeHelp.objects.filter(author=self.request.user)

class FreeHelpDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = FreeHelp
    success_url = reverse_lazy('FacilitiesWelfare:homeFH')
    template_name = "FacilitiesWelfare/FreeHelp/FreeHelp_confirm_delete.html"

class UserFreeHelp(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = FreeHelp
    paginate_by = 10
    template_name = "FacilitiesWelfare/FreeHelp/FreeHelp_list_User.html"

    def get_queryset(self):
        return FreeHelp.objects.filter(Q(IdUser=self.request.user))

    def get_object(self):
        return FreeHelp.objects.get(pk = self.request.user.pk)