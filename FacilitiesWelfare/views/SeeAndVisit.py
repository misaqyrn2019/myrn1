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

class SeeAndVisitList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = SeeAndVisit
    paginate_by = 10
    template_name = "FacilitiesWelfare/SeeAndVisit/SeeAndVisit_list.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return SeeAndVisit.objects.all()
        elif self.request.User.is_FacilitiesWelfare:
            return SeeAndVisit.objects.filter(author=self.request.user)

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class SeeAndVisitCreate(FacilitiesWelfareAccessMixin,DefineSeeAndVisit,CreateView):
    model = SeeAndVisit
    success_url = reverse_lazy('FacilitiesWelfare:homeSAV')
    template_name = "FacilitiesWelfare/SeeAndVisit/SeeAndVisit-create-update.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return SeeAndVisit.objects.all()
        else:
            return SeeAndVisit.objects.filter(author=self.request.user)

class SeeAndVisitUpdate(FacilitiesWelfareAccessMixin,DefineSeeAndVisit,UpdateView):
    model = SeeAndVisit
    success_url = reverse_lazy('FacilitiesWelfare:homeSAV')
    template_name = "FacilitiesWelfare/SeeAndVisit/SeeAndVisit-create-update.html"

    def get_queryset(self):
        if self.request.user.is_FacilitiesWelfare:
            return SeeAndVisit.objects.all()
        else:
            return SeeAndVisit.objects.filter(author=self.request.user)

class SeeAndVisitDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = SeeAndVisit
    success_url = reverse_lazy('FacilitiesWelfare:homeSAV')
    template_name = "FacilitiesWelfare/SeeAndVisit/SeeAndVisit_confirm_delete.html"

class SeeAndVisitUser(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = SeeAndVisit
    paginate_by = 10
    template_name = "FacilitiesWelfare/SeeAndVisit/SeeAndVisit_list_User.html"

    def get_queryset(self):
        return SeeAndVisit.objects.filter(IdUser=self.request.user)

    def get_object(self):
        return SeeAndVisit.objects.get(pk = self.request.user.pk)