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

class ProjectList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = Project
    paginate_by = 10
    template_name = "FacilitiesWelfare/Projects/Projects_list.html"

    def get_queryset(self):
        return Project.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class ProjectCreate(FacilitiesWelfareAccessMixin,DefineProjects,CreateView):
    model = Project
    success_url = reverse_lazy('FacilitiesWelfare:homeFPR')
    template_name = "FacilitiesWelfare/Projects/Projects-create-update.html"

    def get_queryset(self):
        return Project.objects.all()

class ProjectUpdate(FacilitiesWelfareAccessMixin,DefineProjects,UpdateView):
    model = Project
    success_url = reverse_lazy('FacilitiesWelfare:homeFPR')
    template_name = "FacilitiesWelfare/Projects/Projects-create-update.html"

    def get_queryset(self):
        return Project.objects.all()

class ProjectDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = Project
    success_url = reverse_lazy('FacilitiesWelfare:homeFPR')
    template_name = "FacilitiesWelfare/Projects/Projects_confirm_delete.html"

class UserProjectListAll(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Project
    paginate_by = 10
    template_name = "FacilitiesWelfare/Projects/Projects_list_User.html"

    def get_queryset(self):
        return Project.objects.all()

class UserRegProject(LoginRequiredMixin,ListView):
    model = RegisterProject
    template_name = "FacilitiesWelfare/Projects/Projects-Save.html"

    def get_queryset(self,**kwargs):
        pk=self.kwargs.get('pk')
        return pk

class UserRegProject2(LoginRequiredMixin,DefineRegisterProjects,CreateView):
    model = RegisterProject
    success_url = reverse_lazy('FacilitiesWelfare:Projects-User')

class UserRegisteryProjects(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = RegisterProject
    paginate_by = 10
    template_name = "FacilitiesWelfare/Projects/Projects_User_Registry.html"

    def get_queryset(self):
        return RegisterProject.objects.filter(Q(IdUser=self.request.user.pk))

class ProjectsDelUser(LoginRequiredMixin,DeleteView):
    model = RegisterProject
    success_url = reverse_lazy('FacilitiesWelfare:Projects-User')
    template_name = "FacilitiesWelfare/Projects/Projects_User_Delete.html"

class TypeProjectList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = TypeProject
    paginate_by = 10
    template_name = "FacilitiesWelfare/Projects/TypeProjects_list.html"

    def get_queryset(self):
        return TypeProject.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class TypeProjectCreate(FacilitiesWelfareAccessMixin,DefineTypeProjects,CreateView):
    model = TypeProject
    success_url = reverse_lazy('FacilitiesWelfare:homeTFPR')
    template_name = "FacilitiesWelfare/Projects/TypeProjects-create-update.html"

    def get_queryset(self):
        return TypeProject.objects.all()

class TypeProjectUpdate(FacilitiesWelfareAccessMixin,DefineTypeProjects,UpdateView):
    model = TypeProject
    success_url = reverse_lazy('FacilitiesWelfare:homeTFPR')
    template_name = "FacilitiesWelfare/Projects/TypeProjects-create-update.html"

    def get_queryset(self):
        return TypeProject.objects.all()

class TypeProjectDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = TypeProject
    success_url = reverse_lazy('FacilitiesWelfare:homeTFPR')
    template_name = "FacilitiesWelfare/Projects/TypeProjects_confirm_delete.html"