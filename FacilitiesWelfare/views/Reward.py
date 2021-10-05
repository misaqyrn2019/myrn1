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

class RewardList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = Reward
    paginate_by = 10
    template_name = "FacilitiesWelfare/Reward/Reward_list.html"

    def get_queryset(self):
        return Reward.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Reward, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class RewardCreate(FacilitiesWelfareAccessMixin,DefineReward,CreateView):
    model = Reward
    success_url = reverse_lazy('FacilitiesWelfare:homeFwR')
    template_name = "FacilitiesWelfare/Reward/Reward-create-update.html"

class RewardUpdate(FacilitiesWelfareAccessMixin,DefineReward,UpdateView):
    model = Reward
    success_url = reverse_lazy('FacilitiesWelfare:homeFwR')
    template_name = "FacilitiesWelfare/Reward/Reward-create-update.html"

class RewardDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = Reward
    success_url = reverse_lazy('FacilitiesWelfare:homeFwR')
    template_name = "FacilitiesWelfare/Reward/Reward_confirm_delete.html"

class UserReward(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Reward
    paginate_by = 10
    template_name = "FacilitiesWelfare/Reward/Reward_list_User.html"

    def get_queryset(self):
        return Reward.objects.filter(IdUser=self.request.user)