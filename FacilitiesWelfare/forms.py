from django import forms
from FacilitiesWelfare.models import *
from django.contrib.auth.forms import UserCreationForm

class DefineProjects(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['Id','Name', 'IdCity','IdTypeProject','Description']

class DefineTypeProjects(forms.ModelForm):
	class Meta:
		model = TypeProject
		fields = ['Id','Name']

class DefineReward(forms.ModelForm):
	class Meta:
		model = Reward
		fields = ['Id','Title','AssignmentDate','Price','Description','IdUser']

class DefineTravels(forms.ModelForm):
	class Meta:
		model = Travels
		fields = ['Id','IdCity','StartDateTime','EndDateTime','Description','status','IdUser']

class DefineLoan(forms.ModelForm):
	class Meta:
		model = Loan
		fields = ['Id','StartDateTime','EndDateTime','TotalAmount', 'NumberInstallment','InstallmentAmount','LoanInterest','Description','status','Title']

class DefineRegisterLoan(forms.ModelForm):
	class Meta:
		model = RegisterLoan
		fields = ['Id','IdLoan','IdUser','statusConfirmation','statusLattery']

class DefineRegisterLoan2(forms.ModelForm):
	class Meta:
		model = RegisterLoan
		fields = ['Id','IdLoan','IdUser']

class DefineRelativesDeathServices(forms.ModelForm):
	class Meta:
		model = RelativesDeathServices
		fields = ['Id','Name','Family','DeathDate','IdUser','Relation','Description']

class DefineOrganizationalHouse(forms.ModelForm):
	class Meta:
		model = OrganizationalHouse
		fields = ['Id','Title','IdCity','Address','PostalCode','Pelaque','Unit','Floor','DateRegister','Description']

class DefineRegisterOrganizationalHouse(forms.ModelForm):
	class Meta:
		model = RegisterOrganizationalHouse
		fields = ['Id','IdUser','IdOrganizationHouse','DateExpire','IsVerify']

class FormRegisterOrganizationalHouse(UserCreationForm):
	class Meta:
		model = RegisterOrganizationalHouse
		fields = ['Id','IdUser','IdOrganizationHouse','DateExpire','IsVerify']

class DefineCachAssistance(forms.ModelForm):
	class Meta:
		model = CashAssistance
		fields = ['Id','TypeAssistance','IdUser','Title','Price','Description','DateRegister']

class DefineSeeAndVisit(forms.ModelForm):
	class Meta:
		model = SeeAndVisit
		fields = ['Id','IdUser','ConsumerItems','Name','Family','Description','DateTimeVisit']

class DefineConsumerItems(forms.ModelForm):
	class Meta:
		model = ConsumerItems
		fields = ['Id','Title','TypeAssistance','Items','Price','DateRegister','DateExpire','Description']

class DefineConsumerItemsRegister(forms.ModelForm):
	class Meta:
		model = ConsumerItemsRegister
		fields = ['Id','IdConsumerItems','IdUser','IsReceived']

class DefineFreeHelp(forms.ModelForm):
	class Meta:
		model = FreeHelp
		fields = ['Id','Title','TypeAssistance','DateRegister','IdUser','Description','Price']

class DefineRegisterProjects(forms.ModelForm):
	class Meta:
		model = RegisterProject
		fields = ['Id','IdUser','IdProject']
