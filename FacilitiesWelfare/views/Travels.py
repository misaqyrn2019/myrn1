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
from django.shortcuts import render, get_object_or_404
from FacilitiesWelfare.models import *
from FacilitiesWelfare.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

class TravelsList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = Travels
    paginate_by = 10
    template_name = "FacilitiesWelfare/Travels/Travels_list.html"

    def get_queryset(self):
        return Travels.objects.all()

    def get_object(self):
        return Travels.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Travels, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class TravelsCreate(FacilitiesWelfareAccessMixin,DefineTravels,CreateView):
    model = Travels
    success_url = reverse_lazy('FacilitiesWelfare:homeFwT')
    template_name = "FacilitiesWelfare/Travels/Travels-create-update.html"

class TravelsUpdate(FacilitiesWelfareAccessMixin,DefineTravels,UpdateView):
    model = Travels
    success_url = reverse_lazy('FacilitiesWelfare:homeFwT')
    template_name = "FacilitiesWelfare/Travels/Travels-create-update.html"

class TravelsDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = Travels
    success_url = reverse_lazy('FacilitiesWelfare:homeFwT')
    template_name = "FacilitiesWelfare/Travels/Travels_confirm_delete.html"

class UserTravels(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Travels
    paginate_by = 10
    template_name = "FacilitiesWelfare/Travels/Travels_list_User.html"

    def get_queryset(self):
        return Travels.objects.filter(IdUser=self.request.user)