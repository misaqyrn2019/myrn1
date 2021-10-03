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
from extensions.utils import jalali_converter
from django.shortcuts import render, get_object_or_404
from FacilitiesWelfare.models import *
from FacilitiesWelfare.forms import *
from datetime import date,datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin

class LoanList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = Loan
    paginate_by = 10
    template_name = "FacilitiesWelfare/Loan/Loan_list.html"

    def get_queryset(self):
        return Loan.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class LoanCreate(FacilitiesWelfareAccessMixin,DefineLoan,CreateView):
    model = Loan
    success_url = reverse_lazy('FacilitiesWelfare:homeFwL')
    template_name = "FacilitiesWelfare/Loan/Loan-create-update.html"

    def get_queryset(self):
        return Loan.objects.all()

class LoanUpdate(FacilitiesWelfareAccessMixin,DefineLoan,UpdateView):
    model = Loan
    success_url = reverse_lazy('FacilitiesWelfare:homeFwL')
    template_name = "FacilitiesWelfare/Loan/Loan-create-update.html"

    def get_queryset(self):
        return Loan.objects.all()

class LoanDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = Loan
    success_url = reverse_lazy('FacilitiesWelfare:homeFwL')
    template_name = "FacilitiesWelfare/Loan/Loan_confirm_delete.html"

class RLoanList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = RegisterLoan
    paginate_by = 10
    template_name = "FacilitiesWelfare/Loan/RegisterLoan_list.html"

    def get_queryset(self):
        return RegisterLoan.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class LoanListForReg(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = Loan
    paginate_by = 10
    template_name = "FacilitiesWelfare/Loan/LoanForRegsiter.html"

    def get_queryset(self):
        return Loan.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class RegisterLoan22(FacilitiesWelfareAccessMixin,DefineRegisterLoan,CreateView):
    model = RegisterLoan
    success_url = reverse_lazy('FacilitiesWelfare:homeFwRL')
    template_name = "FacilitiesWelfare/Loan/RegisterLoan.html"

    def get_queryset(self):
        return RegisterLoan.objects.all()

class UserLoanList(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Loan
    paginate_by = 10
    template_name = "FacilitiesWelfare/Loan/Loan_list_User.html"

    def get_queryset(self):
        return Loan.objects.filter(
            Q(StartDateTime__lte=datetime.today()) & 
            Q(EndDateTime__gte=datetime.today()))

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class UserLoanReg(LoginRequiredMixin,ListView):
    model = Loan
    template_name = "FacilitiesWelfare/Loan/Loan-Save.html"

    def get_queryset(self,**kwargs):
        pk=self.kwargs.get('pk')
        return pk

class UserLoanReg2(LoginRequiredMixin,DefineRegisterLoan2,CreateView):
    model = RegisterLoan
    success_url = reverse_lazy('FacilitiesWelfare:Loan-List-User2')
    
class UserLoanList2(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = RegisterLoan
    paginate_by = 10
    template_name = "FacilitiesWelfare/Loan/Loan_list_User2.html"

    def get_queryset(self):
        return RegisterLoan.objects.filter(
            Q(IdUser=self.request.user)
        )

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class UserLoanDelete(LoginRequiredMixin,DeleteView):
    model = RegisterLoan
    success_url = reverse_lazy('FacilitiesWelfare:Loan-List-User2')
    template_name = "FacilitiesWelfare/Loan/LoanR_confirm_delete.html"