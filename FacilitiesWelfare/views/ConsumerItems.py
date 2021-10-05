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
import datetime
from datetime import date,datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin

class ConsumerItemsList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = ConsumerItems
    paginate_by = 10
    template_name = "FacilitiesWelfare/ConsumerItems/ConsumerItems_list.html"

    def get_queryset(self):
        return ConsumerItems.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(ConsumerItems, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class ConsumerItemsCreate(FacilitiesWelfareAccessMixin,DefineConsumerItems,CreateView):
    model = ConsumerItems
    success_url = reverse_lazy('FacilitiesWelfare:homeCI')
    template_name = "FacilitiesWelfare/ConsumerItems/ConsumerItems-create-update.html"

class ConsumerItemsUpdate(FacilitiesWelfareAccessMixin,DefineConsumerItems,UpdateView):
    model = ConsumerItems
    success_url = reverse_lazy('FacilitiesWelfare:homeCI')
    template_name = "FacilitiesWelfare/ConsumerItems/ConsumerItems-create-update.html"

class ConsumerItemsDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = ConsumerItems
    success_url = reverse_lazy('FacilitiesWelfare:homeCI')
    template_name = "FacilitiesWelfare/ConsumerItems/ConsumerItems_confirm_delete.html"

class UserConsumerItems(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = ConsumerItems
    paginate_by = 10
    template_name = "FacilitiesWelfare/ConsumerItems/ConsumerItems_list_User.html"

    def get_queryset(self):
        return ConsumerItems.objects.filter(
                Q(DateExpire__gte=datetime.today())
            )

    def get_object(self):
        return ConsumerItems.objects.get(pk = self.request.user.pk)