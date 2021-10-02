from django.contrib import admin
from .models import (
	Storeroom,Customer,GroupCommodity,CategoryCommodity,UnitPack,Supplier,UnitofMeasurement,
	drivers,Commodity,EntryCommodity,Transportation,productRepaired,TransfersbetweenStoreroom,
	Receipt,SettlementArrived,PurchaseRequest
	)

admin.site.register(Storeroom)
admin.site.register(Customer)
admin.site.register(GroupCommodity)
admin.site.register(CategoryCommodity)
admin.site.register(UnitPack)
admin.site.register(Supplier)
admin.site.register(UnitofMeasurement)
admin.site.register(drivers)
admin.site.register(Commodity)
admin.site.register(EntryCommodity)
admin.site.register(Transportation)
admin.site.register(productRepaired)
admin.site.register(TransfersbetweenStoreroom)
admin.site.register(Receipt)
admin.site.register(SettlementArrived)
admin.site.register(PurchaseRequest)
