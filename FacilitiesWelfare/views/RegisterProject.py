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

class RegisterProjectList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = RegisterProject
    paginate_by = 10
    template_name = "FacilitiesWelfare/RegisterProjects/RegisterProjects_list.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return RegisterProject.objects.all()
        elif self.request.User.is_FacilitiesWelfare:
            return RegisterProject.objects.filter(author=self.request.user)

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class RegisterProjectCreate(FacilitiesWelfareAccessMixin,DefineRegisterProjects,CreateView):
    model = RegisterProject
    success_url = reverse_lazy('FacilitiesWelfare:homeRPR')
    template_name = "FacilitiesWelfare/RegisterProjects/RegisterProjects-create-update.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return RegisterProject.objects.all()
        else:
            return RegisterProject.objects.filter(author=self.request.user)

class RegisterProjectUpdate(FacilitiesWelfareAccessMixin,DefineRegisterProjects,UpdateView):
    model = RegisterProject
    success_url = reverse_lazy('FacilitiesWelfare:homeRPR')
    template_name = "FacilitiesWelfare/RegisterProjects/RegisterProjects-create-update.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return RegisterProject.objects.all()
        else:
            return RegisterProject.objects.filter(author=self.request.user)

class RegisterProjectDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = RegisterProject
    success_url = reverse_lazy('FacilitiesWelfare:homeRPR')
    template_name = "FacilitiesWelfare/RegisterProjects/RegisterProjects_confirm_delete.html"
