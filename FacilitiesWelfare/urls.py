from django.urls import path
from FacilitiesWelfare.views import *

app_name = "FacilitiesWelfare"
urlpatterns = [
	path('homeFPR', ProjectList.as_view(), name="homeFPR"),
	path('pageFPR/<int:page>', ProjectList.as_view(), name="homeFPR"),
	path('Projects/Create', ProjectCreate.as_view(), name="CreateFPR"),
	path('Projects/delete/<int:pk>', ProjectDelete.as_view(), name="Projects-Delete"),
	path('Projects/update/<int:pk>', ProjectUpdate.as_view(), name="Projects-update"),
	path('homeUFPR', UserProjectListAll.as_view(), name="homeUFPR"),
	path('pageUFPR/<int:page>', UserProjectListAll.as_view(), name="homeUFPR"),
	path('Projects/Projects-Reg-User/<int:pk>', UserRegProject.as_view(), name="Projects-Reg-User"),#User
	path('Projects/Projects-Reg2-User', UserRegProject2.as_view(), name="Projects-Reg2-User"),#User
	path('Projects/Projects-User', UserRegisteryProjects.as_view(), name="Projects-User"),#User
	path('Projects/Projects-User/<int:pk>', UserRegisteryProjects.as_view(), name="Projects-User"),#User
	path('Projects/Projects-Del-User/<int:pk>', ProjectsDelUser.as_view(), name="Projects-Del-User"),#User

	path('homeTFPR', TypeProjectList.as_view(), name="homeTFPR"),
	path('pageTFPR/<int:page>', TypeProjectList.as_view(), name="homeTFPR"),
	path('TypeProjects/CreateT', TypeProjectCreate.as_view(), name="CreateTFPR"),
	path('TypeProjects/delete/<int:pk>', TypeProjectDelete.as_view(), name="TypeProjects-Delete"),
	path('TypeProjects/update/<int:pk>', TypeProjectUpdate.as_view(), name="TypeProjects-update"),

	path('homeFwR', RewardList.as_view(), name="homeFwR"),
	path('pageFwR/<int:page>', RewardList.as_view(), name="homeFwR"),
	path('Reward/CreateR', RewardCreate.as_view(), name="CreateFwR"),
	path('Reward/delete/<int:pk>', RewardDelete.as_view(), name="Reward-Delete"),
	path('Reward/update/<int:pk>', RewardUpdate.as_view(), name="Reward-update"),
	path('Reward/Reward-List-User', UserReward.as_view(), name="Reward-List-User"),#User
	path('Reward/Reward-List-User/<int:page>', UserReward.as_view(), name="Reward-List-User"),#User

	path('homeFwT', TravelsList.as_view(), name="homeFwT"),
	path('pageFwT/<int:page>', TravelsList.as_view(), name="homeFwT"),
	path('Travels/CreateTR', TravelsCreate.as_view(), name="CreateTR"),
	path('Travels/delete/<int:pk>', TravelsDelete.as_view(), name="Travels-Delete"),
	path('Travels/update/<int:pk>', TravelsUpdate.as_view(), name="Travels-update"),
	path('Travels/Travels-List-User', UserTravels.as_view(), name="Travels-List-User"),#User
	path('Travels/Travels-List-User/<int:page>', UserTravels.as_view(), name="Travels-List-User"),#User

	path('homeFwL', LoanList.as_view(), name="homeFwL"),
	path('pageFwL/<int:page>', LoanList.as_view(), name="homeFwL"),
	path('Loan/CreateFwL', LoanCreate.as_view(), name="CreateFwL"),
	path('Loan/delete/<int:pk>', LoanDelete.as_view(), name="Loan-Delete"),
	path('Loan/update/<int:pk>', LoanUpdate.as_view(), name="Loan-update"),

	path('Loan/Loan-List-User', UserLoanList.as_view(), name="Loan-List-User"),
	path('Loan/Loan-List-User/<int:pk>', UserLoanList.as_view(), name="Loan-List-User"),
	path('Loan/Loan-Reg-User/<int:pk>', UserLoanReg.as_view(), name="Loan-Reg-User"),
	path('Loan/Loan-Reg2-User', UserLoanReg2.as_view(), name="Loan-Reg2-User"),
	path('Loan/Loan-List-User2', UserLoanList2.as_view(), name="Loan-List-User2"),
	path('Loan/Loan-List-User2/<int:pk>', UserLoanList2.as_view(), name="Loan-List-User2"),
	path('Loan/Loan-DeleteR-User/<int:pk>', UserLoanDelete.as_view(), name="Loan-DeleteR-User"),

	path('homeRDS', RelativesDeathServicesList.as_view(), name="homeRDS"),
	path('pageRDS/<int:page>', RelativesDeathServicesList.as_view(), name="homeRDS"),
	path('RelativesDeathServices/CreateFwL', RelativesDeathServicesCreate.as_view(), name="CreateRDS"),
	path('RelativesDeathServices/delete/<int:pk>', RelativesDeathServicesDelete.as_view(), name="RelativesDeathServices-Delete"),
	path('RelativesDeathServices/update/<int:pk>', RelativesDeathServicesUpdate.as_view(), name="RelativesDeathServices-update"),
	path('RelativesDeathServices/RelativesDeathServices-List-User', UserRelativesDeathServices.as_view(), name="RelativesDeathServices-List-User"),#User
	path('RelativesDeathServices/RelativesDeathServices-List-User/<int:page>', UserRelativesDeathServices.as_view(), name="RelativesDeathServices-List-User"),#User

	path('homeOH', OrganizationalHouseList.as_view(), name="homeOH"),
	path('pageOH/<int:page>', OrganizationalHouseList.as_view(), name="homeOH"),
	path('OrganizationalHouse/CreateOH', OrganizationalHouseCreate.as_view(), name="CreateOH"),
	path('OrganizationalHouse/delete/<int:pk>', OrganizationalHouseDelete.as_view(), name="OrganizationalHouse-Delete"),
	path('OrganizationalHouse/update/<int:pk>', OrganizationalHouseUpdate.as_view(), name="OrganizationalHouse-update"),
	path('OrganizationalHouse/OrganizationalHouse-List-All', UserOrganizationalHouseListAll.as_view(), name="OrganizationalHouse-List-All"),
	path('OrganizationalHouse/OrganizationalHouse-List-All/<int:pk>', UserOrganizationalHouseListAll.as_view(), name="OrganizationalHouse-List-All"),
	path('OrganizationalHouse/OrganizationalHouse-Reg-User/<int:pk>', OrganizationalHouseRegUser.as_view(), name="OrganizationalHouse-Reg-User"),
	path('OrganizationalHouse/OrganizationalHouse-Reg2-User', OrganizationalHouseRegUser2.as_view(), name="OrganizationalHouse-Reg2-User"),
	path('OrganizationalHouse/OrganizationalHouse-LST-User', OrganizationalHouseListUser.as_view(), name="OrganizationalHouse-LST-User"),
	path('OrganizationalHouse/OrganizationalHouse-LST-User/<int:pk>', OrganizationalHouseListUser.as_view(), name="OrganizationalHouse-LST-User"),

	path('homeROH', RegisterOrganizationalHouseList.as_view(), name="homeROH"),
	path('pageROH/<int:page>', RegisterOrganizationalHouseList.as_view(), name="homeROH"),
	path('RegisterOrganizationalHouse/CreateROH', RegisterOrganizationalHouseCreate.as_view(), name="CreateROH"),
	path('RegisterOrganizationalHouse/delete/<int:pk>', RegisterOrganizationalHouseDelete.as_view(), name="RegisterOrganizationalHouse-Delete"),
	path('RegisterOrganizationalHouse/update/<int:pk>', RegisterOrganizationalHouseUpdate.as_view(), name="RegisterOrganizationalHouse-update"),

	path('homeSAV', SeeAndVisitList.as_view(), name="homeSAV"),
	path('pageSAV/<int:page>', SeeAndVisitList.as_view(), name="homeSAV"),
	path('SeeAndVisit/CreateSAV', SeeAndVisitCreate.as_view(), name="CreateSAV"),
	path('SeeAndVisit/delete/<int:pk>', SeeAndVisitDelete.as_view(), name="SeeAndVisit-Delete"),
	path('SeeAndVisit/update/<int:pk>', SeeAndVisitUpdate.as_view(), name="SeeAndVisit-update"),
	path('SeeAndVisit/SeeAndVisit-List-User', SeeAndVisitUser.as_view(), name="SeeAndVisit-List-User"),#User
	path('SeeAndVisit/SeeAndVisit-List-User/<int:page>', SeeAndVisitUser.as_view(), name="SeeAndVisit-List-User"),#User

	path('homeCA', CashAssistanceList.as_view(), name="homeCA"),
	path('pageCA/<int:page>', CashAssistanceList.as_view(), name="homeCA"),
	path('CashAssistance/CreateCA', CashAssistanceCreate.as_view(), name="CreateCA"),
	path('CashAssistance/delete/<int:pk>', CashAssistanceDelete.as_view(), name="CashAssistance-Delete"),
	path('CashAssistance/update/<int:pk>', CashAssistanceUpdate.as_view(), name="CashAssistance-update"),
	path('CashAssistance/CashAssistance-List-User', UserCashAssistance.as_view(), name="CashAssistance-List-User"),#User
	path('CashAssistance/CashAssistance-List-User/<int:page>', UserCashAssistance.as_view(), name="CashAssistance-List-User"),#User

	path('homeCI', ConsumerItemsList.as_view(), name="homeCI"),
	path('pageCI/<int:page>', ConsumerItemsList.as_view(), name="homeCI"),
	path('ConsumerItems/CreateCI', ConsumerItemsCreate.as_view(), name="CreateCI"),
	path('ConsumerItems/delete/<int:pk>', ConsumerItemsDelete.as_view(), name="ConsumerItems-Delete"),
	path('ConsumerItems/update/<int:pk>', ConsumerItemsUpdate.as_view(), name="ConsumerItems-update"),
	path('ConsumerItems/ConsumerItems-List-User', UserConsumerItems.as_view(), name="ConsumerItems-List-User"),#User
	path('ConsumerItems/ConsumerItems-List-User/<int:page>', UserConsumerItems.as_view(), name="ConsumerItems-List-User"),#User

	path('homeCIR', ConsumerItemsRegisterList.as_view(), name="homeCIR"),
	path('pageCIR/<int:page>', ConsumerItemsRegisterList.as_view(), name="homeCIR"),
	path('ConsumerItemsRegister/CreateCIR', ConsumerItemsRegisterCreate.as_view(), name="CreateCIR"),
	path('ConsumerItemsRegister/delete/<int:pk>', ConsumerItemsRegisterDelete.as_view(), name="ConsumerItemsRegister-Delete"),
	path('ConsumerItemsRegisterUser/delete/<int:pk>', ConsumerItemsRegisterUserDelete.as_view(), name="ConsumerItemsRegister-User-Delete"),
	path('ConsumerItemsRegister/update/<int:pk>', ConsumerItemsRegisterUpdate.as_view(), name="ConsumerItemsRegister-update"),
	path('ConsumerItemsRegister/ConsumerItemsRegister-List-User', UserConsumerItemsRegister.as_view(), name="ConsumerItemsRegister-List-User"),#User
	path('ConsumerItemsRegister/ConsumerItemsRegister-List-User/<int:page>', UserConsumerItemsRegister.as_view(), name="ConsumerItemsRegister-List-User"),#User
	path('ConsumerItemsRegister/ConsumerItemsRegister-Reg-User/<int:pk>', UserRegisterConsumerItems.as_view(), name="ConsumerItemsRegister-Reg-User"),#User
	path('ConsumerItemsRegister/ConsumerItemsRegister-Reg2-User', UserRegisterConsumerItems2.as_view(), name="ConsumerItemsRegister-Reg2-User"),#User

	path('homeFH', FreeHelpList.as_view(), name="homeFH"),
	path('pageFH/<int:page>', FreeHelpList.as_view(), name="homeFH"),
	path('FreeHelp/CreateFH', FreeHelpCreate.as_view(), name="CreateFH"),
	path('FreeHelp/delete/<int:pk>', FreeHelpDelete.as_view(), name="FreeHelp-Delete"),
	path('FreeHelp/update/<int:pk>', FreeHelpUpdate.as_view(), name="FreeHelp-update"),
	path('FreeHelp/FreeHelp-List-User', UserFreeHelp.as_view(), name="FreeHelp-List-User"),#User
	path('FreeHelp/FreeHelp-List-User/<int:page>', UserFreeHelp.as_view(), name="FreeHelp-List-User"),#User

	path('homeRPR', RegisterProjectList.as_view(), name="homeRPR"),
	path('pageRPR/<int:page>', RegisterProjectList.as_view(), name="homeRPR"),
	path('RegisterProjects/CreateRPR', RegisterProjectCreate.as_view(), name="CreateRPR"),
	path('RegisterProjects/delete/<int:pk>', RegisterProjectDelete.as_view(), name="RegisterProjects-Delete"),
	path('RegisterProjects/update/<int:pk>', RegisterProjectUpdate.as_view(), name="RegisterProjects-update"),
]