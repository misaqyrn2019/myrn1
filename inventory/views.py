from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
    Storeroom,GroupCommodity,CategoryCommodity,UnitPack,Supplier,UnitofMeasurement,
    Commodity,GroupCommodity,UnitPack,Customer,drivers,EntryCommodity,Transportation,
    productRepaired,TransfersbetweenStoreroom,Receipt,SettlementArrived,PurchaseRequest
    )
from account.mixins import (
	FieldsMixin,
	FormValidMixin,
	AuthorAccessMixin,
	AuthorsAccessMixin,
	
    StorekeeperUserAccessMixin
)
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
    DetailView
)
from django.views.generic.edit import FormView
from account.models import User
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from account.mixins import AuthorAccessMixin
from django.db.models import Q
from django.utils import timezone
from inventory.forms import (
    DefineStoreroom,
    DefineGroupCommodity,
    Definedrivers,
    DefinedCommodity,
    DefineStoreroom,
    DefinedCustomer,
    DefinedGroupCommodity,
    DefinedUnitofMeasurement,
    DefinedUnitPack,
    DefinedSupplier,
    DefinedEntryCommodity,
    DefinedTransportation,
    DefinedProductRepaired,
    DefinedTransfersbetweenStoreroom,
    DefinedReceipt,
    DefinedSettlementArrived,
    DefinedPurchaseRequest
    )
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework import viewsets
from inventory.serializers import CommoditySerializer
import random
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class Dashboard(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    template_name = "inventory/Dashboard.html"
    model = Storeroom

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Storeroom'] = Storeroom.objects.all()
        context['Supplier'] = Supplier.objects.all()
        context['PurchaseRequestCommodity'] = PurchaseRequest.objects.filter(Status='N').distinct('IdCommodity')
        context['PurchaseRequestStoreroom'] = PurchaseRequest.objects.filter(Status='N').distinct('IdStoreroom')
        context['drivers'] = drivers.objects.all()
        
        context['ReceiptSale'] = Receipt.objects.filter(Type='S')
        context['ReceiptBuy'] = Receipt.objects.filter(Type='B')

        context['ReceiptSaleStoreroom'] = Receipt.objects.distinct('IdStoreroom')
        context['ReceiptBuyStoreroom'] = Receipt.objects.distinct('IdStoreroom')

        context['ReceiptStoreroomSale'] = Receipt.objects.filter(Type='S').distinct('IdStoreroom')
        context['ReceiptStoreroomBuy'] = Receipt.objects.filter(Type='B').distinct('IdStoreroom')

        context['productRepairedN'] = productRepaired.objects.filter(Status='N').distinct('IdStoreroom')

        context['EntryCommodityPerStoreroomInput'] = EntryCommodity.objects.filter(Status='i').distinct('IdStoreroom')
        context['EntryCommodityPerStoreroomOutput'] = EntryCommodity.objects.filter(Status='o').distinct('IdStoreroom')
        context['EntryCommodityPerStoreroomReturned'] = EntryCommodity.objects.filter(Status='r').distinct('IdStoreroom')

        return context

# View Storeroom
class PStoreroomList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Storeroom
    paginate_by = 10
    template_name = "inventory/TransfersbetweenStoreroom/Pstoreroom_list.html"

    @login_required(login_url='/login/')
    def get_queryset(self):
        return Storeroom.objects.all()

    @login_required(login_url='/login/')
    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    @login_required(login_url='/login/')
    def get_form_kwargs(self):
        kwargs = super(Storeroom, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class StoreroomList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Storeroom
    paginate_by = 10
    template_name = "inventory/Storeroom/storeroom_list.html"

    def get_queryset(self):
        return Storeroom.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Storeroom, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class StoreroomCreate(StorekeeperUserAccessMixin,LoginRequiredMixin, DefineStoreroom, CreateView):
    model = Storeroom
    success_url = reverse_lazy('inventory:homeSL')
    template_name = "inventory/Storeroom/Storeroom-create-update.html"

    def get_queryset(self):
        return Storeroom.objects.all()

class StoreroomUpdate(StorekeeperUserAccessMixin,LoginRequiredMixin, DefineStoreroom, UpdateView):
    model = Storeroom
    success_url = reverse_lazy('inventory:homeSL')
    template_name = "inventory/Storeroom/Storeroom-create-update.html"

    def get_queryset(self):
        return Storeroom.objects.all()

class StoreroomDelete(StorekeeperUserAccessMixin,LoginRequiredMixin, DeleteView):
    model = Storeroom
    success_url = reverse_lazy('inventory:homeSL')
    template_name = "inventory/Storeroom/Storeroom_confirm_delete.html"

class StoreroomListReport(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    template_name = "inventory/Storeroom/Storeroom_list_Report.html"
    model = Commodity
    lookup_field = "IdStoreroom"

    def get_context_data(self, **kwargs):
        ListPrice = []
        IdStoreroom = self.kwargs.get('IdStoreroom')
        
        for item in Commodity.objects.filter(IdStoreroom=IdStoreroom):
            ListPrice.append(item.UnitPrice * item.UnitPackCount)

        context = super().get_context_data(**kwargs)
        context['ListCommodity'] = Commodity.objects.filter(IdStoreroom=IdStoreroom)
        context['StoreroomName'] = Storeroom.objects.filter(Id=IdStoreroom)[0]
        context['SumPrice'] = sum(ListPrice)
        context['ListPrice'] = ListPrice

        return context

# View Customer
class CustomerList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    model = Customer
    paginate_by = 10
    template_name = "inventory/Customer/list.html"

    def get_queryset(self):
        return Customer.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Customer, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class CustomerCreate(StorekeeperUserAccessMixin,LoginRequiredMixin, DefinedCustomer, CreateView):
    model = Customer
    success_url = reverse_lazy('inventory:homeCU')
    template_name = "inventory/Customer/create-update.html"

    def get_queryset(self):
        return Customer.objects.all()

class CustomerUpdate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedCustomer, UpdateView):
    model = Customer
    success_url = reverse_lazy('inventory:homeCU')
    template_name = "inventory/Customer/create-update.html"

    def get_queryset(self):
        return Customer.objects.all()

class CustomerDelete(StorekeeperUserAccessMixin,LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('inventory:homeCU')
    template_name = "inventory/Customer/confirm_delete.html"

class CustomerListReport(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    template_name = "inventory/Customer/Customer_list_Report.html"
    model = Customer

    def get_queryset(self):
        return Customer.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Customer, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

#GroupCommodity
class GroupCommodityList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    model = GroupCommodity
    paginate_by = 10
    template_name = "inventory/GroupCommodity/list.html"

    def get_queryset(self):
        return GroupCommodity.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(GroupCommodity, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class GroupCommodityCreate(StorekeeperUserAccessMixin,LoginRequiredMixin, DefinedGroupCommodity, CreateView):
    model = GroupCommodity
    success_url = reverse_lazy('inventory:homeGC')
    template_name = "inventory/GroupCommodity/create-update.html"

    def get_queryset(self):
        return GroupCommodity.objects.all()

class GroupCommodityUpdate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedGroupCommodity, UpdateView):
    model = GroupCommodity
    success_url = reverse_lazy('inventory:homeGC')
    template_name = "inventory/GroupCommodity/create-update.html"

    def get_queryset(self):
        return GroupCommodity.objects.all()

class GroupCommodityDelete(StorekeeperUserAccessMixin,LoginRequiredMixin, DeleteView):
    model = GroupCommodity
    success_url = reverse_lazy('inventory:homeGC')
    template_name = "inventory/GroupCommodity/confirm_delete.html"

    def get_queryset(self):
        return GroupCommodity.objects.all()

#CategoryCommodity
class CategoryCommodityList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    model = CategoryCommodity
    paginate_by = 10
    template_name = "inventory/CategoryCommodity/list.html"

    def get_queryset(self):
        return CategoryCommodity.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(CategoryCommodity, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class CategoryCommodityCreate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefineGroupCommodity, CreateView):
    model = CategoryCommodity
    success_url = reverse_lazy('inventory:homeCC')
    template_name = "inventory/CategoryCommodity/create-update.html"

    def get_queryset(self):
        return CategoryCommodity.objects.all()

class CategoryCommodityUpdate(StorekeeperUserAccessMixin,DefineGroupCommodity, UpdateView):
    model = CategoryCommodity
    success_url = reverse_lazy('inventory:homeCC')
    template_name = "inventory/CategoryCommodity/create-update.html"

    def get_queryset(self):
        return CategoryCommodity.objects.all()

class CategoryCommodityDelete(StorekeeperUserAccessMixin, LoginRequiredMixin,DeleteView):
    model = CategoryCommodity
    success_url = reverse_lazy('inventory:homeCC')
    template_name = "inventory/CategoryCommodity/confirm_delete.html"

    def get_queryset(self):
        return CategoryCommodity.objects.all()

#UnitPack
class UnitPackList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    model = UnitPack
    paginate_by = 10
    template_name = "inventory/UnitPack/list.html"

    def get_queryset(self):
        return UnitPack.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(UnitPack, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class UnitPackCreate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedUnitPack, CreateView):
    model = UnitPack
    success_url = reverse_lazy('inventory:homeUP')
    template_name = "inventory/UnitPack/create-update.html"

    def get_queryset(self):
        return UnitPack.objects.all()

class UnitPackUpdate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedUnitPack, UpdateView):
    model = UnitPack
    success_url = reverse_lazy('inventory:homeUP')
    template_name = "inventory/UnitPack/create-update.html"

    def get_queryset(self):
        return UnitPack.objects.all()

class UnitPackDelete(StorekeeperUserAccessMixin,LoginRequiredMixin, DeleteView):
    model = UnitPack
    success_url = reverse_lazy('inventory:homeUP')
    template_name = "inventory/UnitPack/confirm_delete.html"

    def get_queryset(self):
        return UnitPack.objects.all()

#Supplier
class SupplierList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    model = Supplier
    paginate_by = 10
    template_name = "inventory/Supplier/list.html"

    def get_queryset(self):
        return Supplier.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Supplier, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class SupplierCreate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedSupplier, CreateView):
    model = Supplier
    success_url = reverse_lazy('inventory:homeSU')
    template_name = "inventory/Supplier/create-update.html"

    def get_queryset(self):
        return Supplier.objects.all()

class SupplierUpdate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedSupplier, UpdateView):
    model = Supplier
    success_url = reverse_lazy('inventory:homeSU')
    template_name = "inventory/Supplier/create-update.html"

    def get_queryset(self):
        return Supplier.objects.all()

class SupplierDelete(StorekeeperUserAccessMixin,LoginRequiredMixin, DeleteView):
    model = Supplier
    success_url = reverse_lazy('inventory:homeSU')
    template_name = "inventory/Supplier/confirm_delete.html"

    def get_queryset(self):
        return Supplier.objects.all()

class SupplierListReport(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    template_name = "inventory/Supplier/Supplier_list_Report.html"
    model = Commodity
    lookup_field = "IdSupplier"

    def get_context_data(self, **kwargs):
        ListPrice = []
        print(self.kwargs.get('IdSupplier'))
        IdSupplier = self.kwargs.get('IdSupplier')
        
        for item in Commodity.objects.filter(IdSupplier=IdSupplier):
            ListPrice.append(item.UnitPrice * item.UnitPackCount)

        context = super().get_context_data(**kwargs)
        context['ListCommodity'] = Commodity.objects.filter(IdSupplier=IdSupplier)
        context['SupplierName'] = Supplier.objects.filter(Id=IdSupplier)[0]
        context['SumPrice'] = sum(ListPrice)
        context['ListPrice'] = ListPrice

        return context

#UnitofMeasurement
class UnitofMeasurementList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    model = UnitofMeasurement
    paginate_by = 10
    template_name = "inventory/UnitofMeasurement/list.html"

    def get_queryset(self):
        return UnitofMeasurement.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(UnitofMeasurement, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class UnitofMeasurementCreate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedUnitofMeasurement, CreateView):
    model = UnitofMeasurement
    success_url = reverse_lazy('inventory:homeUM')
    template_name = "inventory/UnitofMeasurement/create-update.html"

    def get_queryset(self):
        return UnitofMeasurement.objects.all()

class UnitofMeasurementUpdate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedUnitofMeasurement, UpdateView):
    model = UnitofMeasurement
    success_url = reverse_lazy('inventory:homeUM')
    template_name = "inventory/UnitofMeasurement/create-update.html"

    def get_queryset(self):
        return UnitofMeasurement.objects.all()

class UnitofMeasurementDelete(StorekeeperUserAccessMixin,LoginRequiredMixin, DeleteView):
    model = UnitofMeasurement
    success_url = reverse_lazy('inventory:homeUM')
    template_name = "inventory/UnitofMeasurement/confirm_delete.html"

    def get_queryset(self):
        return UnitofMeasurement.objects.all()

#Commodity
class CommodityList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    model = Commodity
    paginate_by = 10
    template_name = "inventory/Commodity/list.html"

    def get_queryset(self):
        return Commodity.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Commodity, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class CommodityCreate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedCommodity, CreateView):
    model = Commodity
    success_url = reverse_lazy('inventory:homeCO')
    template_name = "inventory/Commodity/create-update.html"

    def get_queryset(self):
        return Commodity.objects.all()

class CommodityUpdate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedCommodity, UpdateView):
    model = Commodity
    success_url = reverse_lazy('inventory:homeCO')
    template_name = "inventory/Commodity/create-update.html"

    def get_queryset(self):
        return Commodity.objects.all()

class CommodityDelete(StorekeeperUserAccessMixin,LoginRequiredMixin, DeleteView):
    model = Commodity
    success_url = reverse_lazy('inventory:homeCO')
    template_name = "inventory/Commodity/confirm_delete.html"

    def get_queryset(self):
        return Commodity.objects.all()

class CommodityListReport(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    template_name = "inventory/Commodity/Commodity_list_Report.html"
    model = Commodity
    lookup_field = "IdCommodity"

    def get_context_data(self, **kwargs):
        ListPrice = []
        IdCommodity = self.kwargs.get('IdCommodity')
        
        for item in Commodity.objects.filter(Id=IdCommodity):
            ListPrice.append(item.UnitPrice * item.UnitPackCount)

        context = super().get_context_data(**kwargs)
        context['ListCommodity'] = Commodity.objects.filter(Id=IdCommodity)
        context['CommodityName'] = Commodity.objects.filter(Id=IdCommodity)[0]
        context['SumPrice'] = sum(ListPrice)

        return context

class CommodityAllListReport(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    template_name = "inventory/Commodity/Commodity_AllList_Report.html"
    model = Commodity

    def get_context_data(self, **kwargs):
        ListPrice = []
        IdCommodity = self.kwargs.get('IdCommodity')
        
        for item in Commodity.objects.all():
            ListPrice.append(item.UnitPrice * item.UnitPackCount)

        context = super().get_context_data(**kwargs)
        context['ListCommodity'] = Commodity.objects.all()
        context['SumPrice'] = sum(ListPrice)

        return context

#drivers
class driversList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    model = drivers
    paginate_by = 10
    template_name = "inventory/drivers/list.html"

    def get_queryset(self):
        return drivers.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(drivers, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class driversCreate(StorekeeperUserAccessMixin,LoginRequiredMixin,Definedrivers, CreateView):
    model = drivers
    success_url = reverse_lazy('inventory:homeDL')
    template_name = "inventory/drivers/create-update.html"

    def get_queryset(self):
        return drivers.objects.all()

class driversUpdate(StorekeeperUserAccessMixin,LoginRequiredMixin,Definedrivers, UpdateView):
    model = drivers
    success_url = reverse_lazy('inventory:homeDL')
    template_name = "inventory/drivers/create-update.html"

    def get_queryset(self):
        return drivers.objects.all()

class driversDelete(StorekeeperUserAccessMixin,LoginRequiredMixin, DeleteView):
    model = drivers
    success_url = reverse_lazy('inventory:homeDL')
    template_name = "inventory/drivers/confirm_delete.html"

    def get_queryset(self):
        return drivers.objects.all()

class DriversReport(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    model = drivers
    template_name = "inventory/drivers/Drivers_list_Report.html"

    def get_queryset(self):
        return drivers.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(drivers, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

#EntryCommodity
class EntryCommodityList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    model = EntryCommodity
    paginate_by = 10
    template_name = "inventory/EntryCommodity/list.html"

    def get_queryset(self):
        return EntryCommodity.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(EntryCommodity, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class EntryCommodityCreate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedEntryCommodity, CreateView):
    model = EntryCommodity
    success_url = reverse_lazy('inventory:homeEC')
    template_name = "inventory/EntryCommodity/create-update.html"

    def get_queryset(self):
        return EntryCommodity.objects.all()

class EntryCommodityUpdate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedEntryCommodity, UpdateView):
    model = EntryCommodity
    success_url = reverse_lazy('inventory:homeEC')
    template_name = "inventory/EntryCommodity/create-update.html"

    def get_queryset(self):
        return EntryCommodity.objects.all()

class EntryCommodityDelete(StorekeeperUserAccessMixin,LoginRequiredMixin, DeleteView):
    model = EntryCommodity
    success_url = reverse_lazy('inventory:homeEC')
    template_name = "inventory/EntryCommodity/confirm_delete.html"

    def get_queryset(self):
        return EntryCommodity.objects.all()

class EntryCommodityReport(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    template_name = "inventory/EntryCommodity/EntryCommodityPerStoreroom.html"
    model = EntryCommodity
    lookup_field = 'IdStoreroom'

    def get_context_data(self, **kwargs):
        IdStoreroom = self.kwargs.get('IdStoreroom')
        Type = self.kwargs.get('Type')
        context = super().get_context_data(**kwargs)
        
        if Type == 1:
            context['ECName'] = "ورود"
            context['EntryCommodityPerStoreroom'] = EntryCommodity.objects.filter(IdStoreroom=IdStoreroom,Status='i')
        elif Type == 2:
            context['ECName'] = "خروج"
            context['EntryCommodityPerStoreroom'] = EntryCommodity.objects.filter(IdStoreroom=IdStoreroom,Status='o')
        elif Type == 3:
            context['ECName'] = "مرجوعی"
            context['EntryCommodityPerStoreroom'] = EntryCommodity.objects.filter(IdStoreroom=IdStoreroom,Status='r')

        return context
#Transportation
class TransportationList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    model = Transportation
    paginate_by = 10
    template_name = "inventory/Transportation/list.html"

    def get_queryset(self):
        return Transportation.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Transportation, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class TransportationCreate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedTransportation, CreateView):
    model = Transportation
    success_url = reverse_lazy('inventory:homeTP')
    template_name = "inventory/Transportation/create-update.html"

    def get_queryset(self):
        return Transportation.objects.all()

class TransportationUpdate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedTransportation, UpdateView):
    model = Transportation
    success_url = reverse_lazy('inventory:homeTP')
    template_name = "inventory/Transportation/create-update.html"

    def get_queryset(self):
        return Transportation.objects.all()

class TransportationDelete(StorekeeperUserAccessMixin,LoginRequiredMixin, DeleteView):
    model = Transportation
    success_url = reverse_lazy('inventory:homeTP')
    template_name = "inventory/Transportation/confirm_delete.html"

    def get_queryset(self):
        return Transportation.objects.all()

#ProductRepaired
class ProductRepairedList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    model = productRepaired
    paginate_by = 10
    template_name = "inventory/productRepaired/list.html"

    def get_queryset(self):
        return productRepaired.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(productRepaired, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class ProductRepairedCreate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedProductRepaired, CreateView):
    model = productRepaired
    success_url = reverse_lazy('inventory:homePR')
    template_name = "inventory/productRepaired/create-update.html"

    def get_queryset(self):
        return productRepaired.objects.all()

class ProductRepairedUpdate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedProductRepaired, UpdateView):
    model = productRepaired
    success_url = reverse_lazy('inventory:homePR')
    template_name = "inventory/productRepaired/create-update.html"

    def get_queryset(self):
        return productRepaired.objects.all()

class ProductRepairedDelete(StorekeeperUserAccessMixin,LoginRequiredMixin, DeleteView):
    model = productRepaired
    success_url = reverse_lazy('inventory:homePR')
    template_name = "inventory/productRepaired/confirm_delete.html"

    def get_queryset(self):
        return productRepaired.objects.all()

class ProductPerStoreroom(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    template_name = "inventory/productRepaired/ProductPerStoreroom.html"
    model = productRepaired
    lookup_field = 'IdStoreroom'

    def get_context_data(self, **kwargs):
        IdStoreroom = self.kwargs.get('IdStoreroom')
        context = super().get_context_data(**kwargs)
        context['productRepaired'] = productRepaired.objects.filter(IdStoreroom=IdStoreroom,Status='N')

        return context

#Receipt
class ReceiptList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    model = Receipt
    paginate_by = 10
    template_name = "inventory/Receipt/list.html"

    def get_queryset(self):
        return Receipt.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Receipt, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class ReceiptCreate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedReceipt, CreateView):
    model = Receipt
    success_url = reverse_lazy('inventory:homeRE')
    template_name = "inventory/Receipt/create-update.html"

    def get_queryset(self):
        return Receipt.objects.all()

class ReceiptUpdate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedReceipt, UpdateView):
    model = Receipt
    success_url = reverse_lazy('inventory:homeRE')
    template_name = "inventory/Receipt/create-update.html"

    def get_queryset(self):
        return Receipt.objects.all()

class ReceiptDelete(StorekeeperUserAccessMixin,LoginRequiredMixin, DeleteView):
    model = Receipt
    success_url = reverse_lazy('inventory:homeRE')
    template_name = "inventory/Receipt/confirm_delete.html"

    def get_queryset(self):
        return Receipt.objects.all()

class ReceiptReportBuy(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    template_name = "inventory/Receipt/ListBuy.html"
    model = Receipt

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ReceiptBuy'] = Receipt.objects.filter(Type='B')

        return context

class ReceiptReportSale(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    template_name = "inventory/Receipt/ListSale.html"
    model = Receipt

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ReceiptSale'] = Receipt.objects.filter(Type='S')

        return context

class ReceiptReportStoreroomSale(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    template_name = "inventory/Receipt/ListReportStoreroomSale.html"
    model = Receipt
    lookup_field = 'IdStoreroom'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        IdStoreroom = self.kwargs.get('IdStoreroom')
        StoreroomSalePrice = []

        context['StoreroomName'] = Receipt.objects.filter(Type='S',IdStoreroom=IdStoreroom).distinct('IdStoreroom')[0]
        
        ItemsSale = Receipt.objects.filter(Type='S',IdStoreroom=IdStoreroom).distinct('IdStoreroom')
        context['ReceiptStoreroomSale'] = ItemsSale
        for item in ItemsSale:
            StoreroomSalePrice.append(item.AmountAfter)
        context['ReceiptStoreroomSalePrice'] = sum(StoreroomSalePrice)

        return context

class ReceiptReportStoreroomBuy(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    template_name = "inventory/Receipt/ListReportStoreroomBuy.html"
    model = Receipt
    lookup_field = 'IdStoreroom'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        IdStoreroom = self.kwargs.get('IdStoreroom')
        StoreroomBuyPrice = []

        context['StoreroomName'] = Storeroom.objects.filter(Id=IdStoreroom)
        itemBuy = Receipt.objects.filter(Type='B',IdStoreroom=IdStoreroom).distinct('IdStoreroom')
        context['ReceiptStoreroomBuy'] = itemBuy
        for item in itemBuy:
            StoreroomBuyPrice.append(item.AmountAfter)
        context['ReceiptStoreroomBuyPrice'] = sum(StoreroomBuyPrice)

        return context
#SettlementArrived
class SettlementArrivedList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    model = SettlementArrived
    paginate_by = 10
    template_name = "inventory/SettlementArrived/list.html"

    def get_queryset(self):
        return SettlementArrived.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(SettlementArrived, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class SettlementArrivedCreate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedSettlementArrived, CreateView):
    model = SettlementArrived
    success_url = reverse_lazy('inventory:homeSA')
    template_name = "inventory/SettlementArrived/create-update.html"

    def get_queryset(self):
        return SettlementArrived.objects.all()

class SettlementArrivedUpdate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedSettlementArrived, UpdateView):
    model = SettlementArrived
    success_url = reverse_lazy('inventory:homeSA')
    template_name = "inventory/SettlementArrived/create-update.html"

    def get_queryset(self):
        return SettlementArrived.objects.all()

class SettlementArrivedDelete(StorekeeperUserAccessMixin,LoginRequiredMixin, DeleteView):
    model = SettlementArrived
    success_url = reverse_lazy('inventory:homeSA')
    template_name = "inventory/SettlementArrived/confirm_delete.html"

    def get_queryset(self):
        return SettlementArrived.objects.all()

#PurchaseRequest
class PurchaseRequestList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    model = PurchaseRequest
    paginate_by = 10
    template_name = "inventory/PurchaseRequest/list.html"

    def get_queryset(self):
        return PurchaseRequest.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(PurchaseRequest, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class PurchaseRequestCreate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedPurchaseRequest, CreateView):
    model = PurchaseRequest
    success_url = reverse_lazy('inventory:homePPR')
    template_name = "inventory/PurchaseRequest/create-update.html"

    def get_queryset(self):
        return PurchaseRequest.objects.all()

class PurchaseRequestUpdate(StorekeeperUserAccessMixin,LoginRequiredMixin,DefinedPurchaseRequest, UpdateView):
    model = PurchaseRequest
    success_url = reverse_lazy('inventory:homePPR')
    template_name = "inventory/PurchaseRequest/create-update.html"

    def get_queryset(self):
        return PurchaseRequest.objects.all()

class PurchaseRequestDelete(StorekeeperUserAccessMixin,LoginRequiredMixin, DeleteView):
    model = PurchaseRequest
    success_url = reverse_lazy('inventory:homePPR')
    template_name = "inventory/PurchaseRequest/confirm_delete.html"

    def get_queryset(self):
        return PurchaseRequest.objects.all()

class PurchaseRequestListReport(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    template_name = "inventory/PurchaseRequest/PurchaseRequest_listCommodity_Report.html"
    model = PurchaseRequest
    lookup_field = "IdCommodity"

    def get_context_data(self, **kwargs):
        ListPrice = []
        IdCommodity = self.kwargs.get('IdCommodity')
        
        for item in PurchaseRequest.objects.filter(IdCommodity=IdCommodity,Status='N'):
            ListPrice.append(item.Count * item.IdCommodity.UnitPrice)
        LP = tuple(ListPrice)
        context = super().get_context_data(**kwargs)
        context['ListCommodity'] = PurchaseRequest.objects.filter(IdCommodity=IdCommodity,Status='N')
        context['StoreroomName'] = PurchaseRequest.objects.filter(IdCommodity=IdCommodity,Status='N')[0]
        context['SumPrice'] = sum(ListPrice)

        return context

class PurchaseRequestListSRReport(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    template_name = "inventory/PurchaseRequest/PurchaseRequest_listStoreroom_Report.html"
    model = PurchaseRequest
    lookup_field = "IdStoreroom"

    def get_context_data(self, **kwargs):
        ListPrice = []
        IdStoreroom = self.kwargs.get('IdStoreroom')
        
        for item in PurchaseRequest.objects.filter(IdStoreroom=IdStoreroom,Status='N'):
            ListPrice.append(item.Count * item.IdCommodity.UnitPrice)

        context = super().get_context_data(**kwargs)
        context['ListCommodity'] = PurchaseRequest.objects.filter(IdStoreroom=IdStoreroom,Status='N')
        context['StoreroomName'] = PurchaseRequest.objects.filter(IdStoreroom=IdStoreroom,Status='N')[0]
        context['SumPrice'] = sum(ListPrice)
        context['ListPrice'] = ListPrice

        return context

#API View
class storeroomList(StorekeeperUserAccessMixin,LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Storeroom
    paginate_by = 10
    template_name = "inventory/Storeroom/storeroom_list.html"

    def get_queryset(self):
        return Storeroom.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Storeroom, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class CommodityPriceByStoreroom(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    def get(self,request, format=None):
        Data = []
        NData = []
        StoreroomOne = Storeroom.objects.all()
        for item in StoreroomOne:
            COM = Commodity.objects.filter(IdStoreroom=item.Id)
            DataPrice = []
            NData.append(item.Name)
            for i in COM:
                DataPrice.append(i.amount)
            SumPrice = sum(DataPrice)
            Data.append(SumPrice)
        Dict = {"Name":NData,
                "Price":Data}
        return Response(Dict)

class PurchaseBuyNPriceByStoreroom(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    def get(self,request, format=None):
        Data = []
        NData = []
        StoreroomOne = Storeroom.objects.all()
        for item in StoreroomOne:
            COM = PurchaseRequest.objects.filter(IdStoreroom=item.Id)
            DataPrice = []
            NData.append(item.Name)
            for i in COM:
                if(i.Status=='N'):
                    DataPrice.append(i.amount)
            SumPrice = sum(DataPrice)
            Data.append(SumPrice)
        Dict = {"Name":NData,
                "Price":Data}
        return Response(Dict)

class PurchaseBuyYPriceByStoreroom(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    def get(self,request, format=None):
        Data = []
        NData = []
        StoreroomOne = Storeroom.objects.all()
        for item in StoreroomOne:
            COM = PurchaseRequest.objects.filter(IdStoreroom=item.Id)
            DataPrice = []
            NData.append(item.Name)
            for i in COM:
                if(i.Status=='Y'):
                    DataPrice.append(i.amount)
            SumPrice = sum(DataPrice)
            Data.append(SumPrice)
        Dict = {"Name":NData,
                "Price":Data}
        return Response(Dict)