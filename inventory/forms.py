from django import forms
from inventory.models import (
	Storeroom,
	GroupCommodity,
	drivers,
	Commodity,
	Customer,
	UnitofMeasurement,
	UnitPack,
	Supplier,
	EntryCommodity,
	Transportation,
	productRepaired,
	TransfersbetweenStoreroom,
	Receipt,
	SettlementArrived,
	PurchaseRequest
	)

class DefineStoreroom(forms.ModelForm):
	class Meta:
		model = Storeroom
		fields = ['Id','Name', 'IdCity', 'Address','status','Telephone']

class DefineGroupCommodity(forms.ModelForm):
	class Meta:
		model = GroupCommodity
		fields = ['Id', 'Name']

class Definedrivers(forms.ModelForm):
	class Meta:
		model = drivers
		fields = ['DriverCode','Name','Family','Telephone','NationalCode','LicensePlateNumber','CarType',
				  'FreightName','AccountNumber','Shabanumber','CardNumber','Address','Description']

class DefinedCommodity(forms.ModelForm):
	class Meta:
		model = Commodity
		fields = [
			'Id','IdStoreroom','Name','IdGroup','IdCategory','IdUnitPack',
			'UnitPackCount','CommoditySpecifications','ExpirationDate',
			'IdSupplier','IdUnitofMeasurement','OrderPoint','MinimumInventory',
			'OrderAmount','MaximumInventory','AddressCommodity','TechnicalNumber','BarCodeText',
			'BarCodeImage','TechnicalSpecifications','UnitPrice','Description',
		]

class DefinedCustomer(forms.ModelForm):
	class Meta:
		model = Customer
		fields = [
			'AccountSideCode','Name','Family',
			'Mobile','TelephoneCustomer','RegistrationNumber',
			'FirstBalanceCourse','EconomicNumber','Status',
			'NationalID','PostalCode','Address'
		]

class DefinedGroupCommodity(forms.ModelForm):
	class Meta:
		model = GroupCommodity
		fields = [
			'Id', 'Name',
		]

class DefinedUnitofMeasurement(forms.ModelForm):
	class Meta:
		model = UnitofMeasurement
		fields = [
			'Id', 'Name',
		]

class DefinedUnitPack(forms.ModelForm):
	class Meta():
		model = UnitPack
		fields = [
			'Id', 'Name',
		]

class DefinedSupplier(forms.ModelForm):
	class Meta:
		model = Supplier
		fields = [
			'Id', 'Name',
		]

class DefinedEntryCommodity(forms.ModelForm):
	class Meta:
		model = EntryCommodity
		fields = [
			'Id', 'IdCommodity','Status','IdStoreroom','Count','DateEntry','Description','IdCustomer','Serial','DateExpired'
		]

class DefinedTransportation(forms.ModelForm):
	class Meta:
		model = Transportation
		fields = ['Id','IdDrivers','Sender','FreightNumber','Transferee','SourceAddress','Description','IdEntryCommodity']

class DefinedProductRepaired(forms.ModelForm):
	class Meta:
		model = productRepaired
		fields = ['Id','IdCommodity','IdCustomer','SerialNumber','DateDelivery','Description','IdStoreroom','Status']

class DefinedTransfersbetweenStoreroom(forms.ModelForm):
	class Meta:
		model = TransfersbetweenStoreroom
		fields = ['Id','IdStoreroomSource','IdStoreroomDestination','Description']

class DefinedReceipt(forms.ModelForm):
	class Meta:
		model = Receipt
		fields = ['Id','IdCommodity','IdStoreroom','IdUnitofMeasurement','Count','Amount','Discount','Taxation','IdCustomer','Type']

class DefinedSettlementArrived(forms.ModelForm):
	class Meta:
		model = SettlementArrived
		fields = ['Id','Type','Amount','Description','Address','Telephone','ReceiptNumber','IdStoreroom']

class DefinedPurchaseRequest(forms.ModelForm):
	class Meta:
		model = PurchaseRequest
		fields = ['Id','IdCommodity','IdUnitofMeasurement','Count','DateRequired','IdStoreroom','TechnicalSpecifications','PurchaseSource','PurchasingOfficer','Status']