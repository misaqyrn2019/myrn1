from django.db.models.query_utils import select_related_descend
from django.shortcuts import render,redirect
from django.urls import reverse
from account.mixins import (
	FieldsMixin,
	FormValidMixin,
	AuthorAccessMixin,
	AuthorsAccessMixin,
	SuperUserAccessMixin,
    FacilitiesWelfareAccessMixin,
    AAMixin,
    FWAccessMixin
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
from account.models import *
from django.contrib.auth.mixins import LoginRequiredMixin

class ConsumerItemsRegisterList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = ConsumerItemsRegister
    paginate_by = 10
    template_name = "FacilitiesWelfare/ConsumerItemsRegister/ConsumerItemsRegister_list.html"

    def get_queryset(self):
        return ConsumerItemsRegister.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(ConsumerItemsRegister, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class ConsumerItemsRegisterCreate(FacilitiesWelfareAccessMixin,DefineConsumerItemsRegister,CreateView):
    model = ConsumerItemsRegister
    success_url = reverse_lazy('FacilitiesWelfare:homeCIR')
    template_name = "FacilitiesWelfare/ConsumerItemsRegister/ConsumerItemsRegister-create-update.html"

class ConsumerItemsRegisterUpdate(FacilitiesWelfareAccessMixin,DefineConsumerItemsRegister,UpdateView):
    model = ConsumerItemsRegister
    success_url = reverse_lazy('FacilitiesWelfare:homeCIR')
    template_name = "FacilitiesWelfare/ConsumerItemsRegister/ConsumerItemsRegister-create-update.html"

class ConsumerItemsRegisterDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = ConsumerItemsRegister
    success_url = reverse_lazy('FacilitiesWelfare:homeCIR')
    template_name = "FacilitiesWelfare/ConsumerItemsRegister/ConsumerItemsRegister_confirm_delete.html"

class ConsumerItemsRegisterUserDelete(FWAccessMixin,DeleteView):
    model = ConsumerItemsRegister
    success_url = reverse_lazy('FacilitiesWelfare:ConsumerItemsRegister-List-User')
    template_name = "FacilitiesWelfare/ConsumerItemsRegister/ConsumerItemsRegisterUser_confirm_delete.html"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        IdConsumerItems = self.kwargs.get('pk')
        IdUser = self.request.user.pk
        User = self.request.user

        ConsumerItemsRegister.objects.filter(
            Q(Id = IdConsumerItems) &
            Q(IdUser = IdUser)
        ).delete()

        return redirect(reverse('FacilitiesWelfare:ConsumerItemsRegister-List-User'))

class UserConsumerItemsRegister(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = ConsumerItemsRegister
    paginate_by = 10
    template_name = "FacilitiesWelfare/ConsumerItemsRegister/ConsumerItemsRegister_list_User.html"

    def get_queryset(self):
        return ConsumerItemsRegister.objects.filter(IdUser=self.request.user)

    def get_object(self):
        return ConsumerItemsRegister.objects.get(pk = self.request.user.pk)

class UserRegisterConsumerItems(LoginRequiredMixin,ListView):
    model = ConsumerItemsRegister
    success_url = reverse_lazy('FacilitiesWelfare:ConsumerItemsRegister-List-User')
    template_name = "FacilitiesWelfare/ConsumerItemsRegister/ConsumerItemsRegister_Save.html"

    def get_queryset(self,**kwargs):
        pk=self.kwargs.get('pk')
        return pk

    def get_object(self):
        pk=self.kwargs.get('pk')
        return ConsumerItemsRegister.objects.get(pk = self.request.user.pk)

class UserRegisterConsumerItems2(LoginRequiredMixin,DefineConsumerItemsRegister,CreateView):
    model = ConsumerItemsRegister
    success_url = reverse_lazy('FacilitiesWelfare:ConsumerItemsRegister-List-User')
    template_name = "FacilitiesWelfare/ConsumerItemsRegister/ConsumerItemsRegister_Save.html"

    def get_queryset(self,**kwargs):
        pk=self.kwargs.get('pk')
        return pk

    def form_valid(self,form):
        form = form.save(commit=False)
        IdConsumerItems = self.request.POST.get('IdConsumerItems')
        IdUser = self.request.POST.get('IdUser')
        ThisItemRegCount = ConsumerItemsRegister.objects.filter(
                Q(IdUser = IdUser) & Q(IdConsumerItems = IdConsumerItems)
            ).count()
        if ThisItemRegCount == 0:
            form.IsReceived = "N"
            form.save()
            return redirect(reverse('FacilitiesWelfare:ConsumerItemsRegister-List-User'))
        else:
            return redirect(reverse('FacilitiesWelfare:ConsumerItemsRegister-List-User'))
