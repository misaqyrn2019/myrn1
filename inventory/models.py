from django.db import models
from extensions.utils import jalali_converter
from account.models import City,Province

# Create your models here.
class Storeroom(models.Model):
    STATUS_Active = (
		('A', 'فعال'),
		('N', "غیرفعال")
	)
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="کدانبار")#کد انبار
    Name = models.CharField(verbose_name="نام انبار",max_length=100)#نام انبار
    IdCity = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name="شهرستان")#شهر انبار
    Address = models.TextField(verbose_name="آدرس انبار")#آدرس انبار
    Telephone = models.CharField(verbose_name="شماره تلفن",max_length=10)#شماره تلفن
    status = models.CharField(max_length=1, choices=STATUS_Active, verbose_name="وضعیت",default="A")

    class Meta:
        verbose_name = "انبار"
        verbose_name_plural="انبار ها"

    def __str__(self):
        return self.Name

class Customer(models.Model):
    StatusBalance = (
        ('A', 'بی حساب'),
        ('B', 'بدهکار'),
        ('C', 'بستانکار'),
    )
    AccountSideCode = models.AutoField(unique=True,primary_key=True,verbose_name="کد طرف حساب")#کد طرف حساب
    Name = models.CharField(verbose_name="نام",max_length=200)#نام
    Family = models.CharField(verbose_name="نام خانوادگی",max_length=200)#نام خانوادگی
    Mobile = models.CharField(verbose_name="شماره موبایل",max_length=10)#شماره موبایل
    TelephoneCustomer = models.CharField(verbose_name="شماره تلفن",max_length=15)#شماره تلفن
    RegistrationNumber = models.CharField(verbose_name="شماره ثبت",max_length=20)#شماره ثبت
    EconomicNumber = models.CharField(verbose_name="کدملی/شماره اقتصادی",max_length=20)#کدملی/شماره اقتصادی
    NationalID = models.CharField(verbose_name="شناسه ملی",max_length=20)#شناسه ملی
    PostalCode = models.CharField(verbose_name="کد پستی",max_length=10)#کد پستی
    Address = models.TextField(verbose_name="آدرس")#آدرس
    FirstBalanceCourse = models.IntegerField(verbose_name="مانده اول دوره")#مانده اول دوره
    Status = models.CharField(max_length=1, choices=StatusBalance, verbose_name="وضعیت حساب",default="A")#وضعیت حساب

    class Meta:
        verbose_name = "نام مشتری"
        verbose_name_plural="مشتری ها"

    def __str__(self):
        return self.Name

class GroupCommodity(models.Model):
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="کد گروه")
    Name = models.CharField(verbose_name="نام گروه",max_length=100)

    class Meta:
        verbose_name = "گروه"
        verbose_name_plural="گروه‏ ها"

    def __str__(self):
        return self.Name

class CategoryCommodity(models.Model):
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="کد دسته")
    Name = models.CharField(verbose_name="نام دسته",max_length=100)

    class Meta:
        verbose_name = "دسته"
        verbose_name_plural="دسته ها"

    def __str__(self):
        return self.Name

class UnitPack(models.Model):
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="کد بسته")
    Name = models.CharField(verbose_name="نام بسته",max_length=100)

    class Meta:
        verbose_name = "بسته"
        verbose_name_plural="بسته ها"

    def __str__(self):
        return self.Name

class Supplier(models.Model):
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="کد تامین کننده")
    Name = models.CharField(verbose_name="نام تامین کننده",max_length=100)

    class Meta:
        verbose_name = "تامین کننده"
        verbose_name_plural="تامین کننده ها"

    def __str__(self):
        return self.Name

class UnitofMeasurement(models.Model):
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="کدواحد سنجش")
    Name = models.CharField(verbose_name="نام واحد سنجش",max_length=100)

    class Meta:
        verbose_name = "واحد سنجش"
        verbose_name_plural="واحدهای سنجش"

    def __str__(self):
        return self.Name

class drivers(models.Model):
    DriverCode = models.AutoField(unique=True,primary_key=True,verbose_name="کد راننده")
    Name = models.CharField(verbose_name="نام",max_length=100)
    Family = models.CharField(verbose_name="نام خانوادگی",max_length=100)
    Telephone = models.CharField(verbose_name="شماره همراه",max_length=10)
    NationalCode = models.CharField(verbose_name="کد ملی",max_length=10) 
    LicensePlateNumber = models.CharField(verbose_name="شماره پلاک",max_length=200) 
    CarType = models.CharField(verbose_name="نوع ماشین",max_length=200) 
    FreightName = models.CharField(verbose_name="نام باربری",max_length=200) 
    AccountNumber = models.CharField(verbose_name="شماره حساب",max_length=20) 
    Shabanumber = models.CharField(verbose_name="شماره شبا",max_length=24) 
    CardNumber = models.CharField(verbose_name="شماره کارت",max_length=16) 
    Address = models.CharField(verbose_name="آدرس",max_length=200)
    Description = models.TextField(verbose_name="توضیحات",max_length=200)

    class Meta:
        verbose_name = "راننده"
        verbose_name_plural="راننده ها"

    def __str__(self):
        return self.Name

class Commodity(models.Model):
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="کد کالا")#کد کالا
    IdStoreroom = models.ForeignKey(Storeroom,on_delete=models.CASCADE,verbose_name="شناسه انبار ")# انبار
    Name = models.CharField(verbose_name="نام کالا",max_length=100)#نام کالا
    IdGroup = models.ForeignKey(GroupCommodity,on_delete=models.CASCADE,verbose_name="شناسه گروه ")# کد گروه - نام گروه
    IdCategory = models.ForeignKey(CategoryCommodity,on_delete=models.CASCADE,verbose_name="شناسه دسته ")# کد دسته - نام دسته
    IdUnitPack = models.ForeignKey(UnitPack,on_delete=models.CASCADE,verbose_name="شناسه بسته ")# واحد بسته
    UnitPackCount = models.IntegerField(verbose_name="مقدار بسته")# مقدار بسته
    CommoditySpecifications = models.TextField(verbose_name="مشخصات کالا")# مشخصات کالا
    ExpirationDate = models.DateField(verbose_name="تاریخ مصرف")# تاریخ مصرف
    IdSupplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,verbose_name="شناسه تامین کننده ")# تامین کننده
    IdUnitofMeasurement = models.ForeignKey(UnitofMeasurement,on_delete=models.CASCADE,verbose_name="کد واحد سنجش")#کد واحد اندازه گیری
    OrderPoint = models.IntegerField(verbose_name="نقطه سفارش") # نقطه سفارش
    MinimumInventory= models.IntegerField(verbose_name="حداقل موجودی")# حداقل موجودی
    OrderAmount = models.IntegerField(verbose_name="میزان سفارش")# میزان سفارش
    MaximumInventory= models.IntegerField(verbose_name="حداکثر موجودی")# حداکثر موجودی
    AddressCommodity = models.TextField(verbose_name="آدرس کالا")# آدرس کالا
    TechnicalNumber =  models.CharField(verbose_name="شماره فنی",max_length=100)# شماره فنی
    BarCodeText = models.CharField(verbose_name="بارکد",max_length=255)#بارکدمتن
    BarCodeImage = models.CharField(verbose_name="بارکد",max_length=255)#بارکدمتن
    TechnicalSpecifications = models.TextField(blank=True,verbose_name="مشخصات فنی")# مشخصات فنی
    EntryDateTime = models.DateTimeField(auto_now=True)#تاریخ ورود کالا
    UnitPrice = models.IntegerField(verbose_name="بهای واحد")#بهای واحد
    Description = models.TextField(blank=True,verbose_name="توضیحات")#توضیحات

    @property
    def amount(self):
        return self.UnitPackCount * self.UnitPrice
    
    class Meta:
        verbose_name = "کالا"
        verbose_name_plural="کالا ها"

    def jEntryDateTime(self):
        return jalali_converter(self.EntryDateTime)
    jEntryDateTime.short_description = "تاریخ ورود"

    def __str__(self):
        return self.Name

class EntryCommodity(models.Model):
    STATUS_CHOICES = (
		('i', 'ورود'),      # Input
		('o', "خروج"),      # Output
        ('r', "مرجوعی"),    # returned
	)
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="کد کالا")# کد کالا
    IdCommodity = models.ForeignKey(Commodity,on_delete=models.CASCADE,verbose_name="نام کالا")# نام کالا
    IdStoreroom = models.ForeignKey(Storeroom,on_delete=models.CASCADE,verbose_name="نام انبار")# نام انبار
    Count = models.IntegerField(verbose_name="تعداد")# تعداد
    DateEntry = models.DateTimeField(verbose_name="تاریخ")# تاریخ
    Description = models.TextField(verbose_name="توضیحات")# توضیحات
    IdCustomer = models.ForeignKey(Customer,on_delete=models.CASCADE,verbose_name="نام مشتری")# نام مشتری
    InvoiceNumber = models.CharField(max_length=200,verbose_name="شماره فاکتور")#شماره فاکتور
    Serial = models.CharField(max_length=200,verbose_name="سریال کالا")#سریال کالا
    DateExpired = models.DateTimeField(verbose_name="تاریخ انقضا")# تاریخ انقضا
    Status = models.CharField(default='i',max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    def jDateExpired(self):
        return jalali_converter(self.DateExpired)
    jDateExpired.short_description = "تاریخ انقضا"

    def jDateEntry(self):
        return jalali_converter(self.DateEntry)
    jDateEntry.short_description = "تاریخ ورود کالا"

    class Meta:
        verbose_name = "ورود کالا"
        verbose_name_plural="ورود کالاها"

    def __str__(self):
        strId = " " + str(self.Id)
        State = self.Status
        
        if State == "i":
            return strId + " " + self.IdCommodity.Name + " " + "ورود کالا"
        elif State == "o":
            return strId + " " + self.IdCommodity.Name + " " + "خروج کالا"
        elif State == "r":
            return strId + " " + self.IdCommodity.Name + " " + "مرجوعی کالا"

class Transportation(models.Model):
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="کد حمل و نقل")# کد حمل و نقل
    IdDrivers = models.ForeignKey(drivers,on_delete=models.CASCADE,verbose_name="نام راننده")# نام راننده
    IdEntryCommodity = models.ForeignKey(EntryCommodity,on_delete=models.CASCADE,verbose_name="ورود کالا")# ورود کالا
    Sender = models.CharField(max_length=200,verbose_name="فرستنده")#فرستنده
    Transferee = models.CharField(max_length=200,verbose_name="گیرنده")#گیرنده
    FreightNumber = models.IntegerField(verbose_name="شماره بارنامه")# شماره بارنامه
    SourceAddress = models.CharField(max_length=200,verbose_name="آدرس مبدا")#آدرس مبدا
    Date = models.DateTimeField(auto_now=True,verbose_name="تاریخ ثبت")# تاریخ ثبت
    Description = models.TextField(verbose_name="توضیحات")# توضیحات

    class Meta:
        verbose_name = "حمل و نقل"
        verbose_name_plural="حمل و نقل"

    def __str__(self):
        return self.Sender

    def jDate(self):
        return jalali_converter(self.Date)
    jDate.short_description = "زمان حمل و نقل"

class productRepaired(models.Model):
    STATUS_CHOICES = (
		('Y', 'تعمیر شده'),
		('N', "تعمیر نشده"),
	)
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="کد تعمیر")# کد تعمیر
    IdStoreroom = models.ForeignKey(Storeroom,on_delete=models.CASCADE,verbose_name="نام انبار")# نام انبار
    IdCommodity = models.ForeignKey(Commodity,on_delete=models.CASCADE,verbose_name="نام کالا")# نام کالا 
    IdCustomer = models.ForeignKey(Customer,on_delete=models.CASCADE,verbose_name="نام مشتری")#نام مشتری 
    SerialNumber = models.CharField(max_length=200,verbose_name="سریال کالا") #شماره سریال 
    DateRegistration = models.DateTimeField(auto_now=True,verbose_name="تاریخ ثبت")#تاریخ ثبت 
    DateDelivery = models.DateTimeField(verbose_name="تاریخ تحویل")#تاریخ تحویل 
    Description = models.TextField(verbose_name="توضیحات",max_length=200)#توضیحات
    Status = models.CharField(default='N',max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    def jDateDelivery(self):
        return jalali_converter(self.DateDelivery)
    jDateDelivery.short_description = "تاریخ تحویل"

    def jDateRegistration(self):
        return jalali_converter(self.DateRegistration)
    jDateRegistration.short_description = "تاریخ ثبت"

    class Meta:
        verbose_name = "تعمیر کالا"
        verbose_name_plural="تعمیر کالاها"

    def __str__(self):
        return self.Status

class TransfersbetweenStoreroom(models.Model):
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="شناسه انتقال")# شناسه انتقال
    Date = models.DateTimeField(auto_now=True,verbose_name="تاریخ ثبت")# تاریخ
    IdStoreroomSource = models.ForeignKey(Storeroom,on_delete=models.CASCADE,verbose_name="انبار مبدا",related_name="StoreroomSource")# انبار مبدا
    IdStoreroomDestination = models.ForeignKey(Storeroom,on_delete=models.CASCADE,verbose_name="انبار مقصد", related_name="StoreroomDestination")# انبار مقصد
    Description = models.TextField(verbose_name="توضیحات",max_length=200)# توضیحات

    class Meta:
        verbose_name = "شناسه انتقال"
        verbose_name_plural="نقل و انتقال"

    def jDate(self):
        return jalali_converter(self.Date)
    jDate.short_description = "تاریخ ثبت"

    def __str__(self):
        return self.Date

class Receipt(models.Model):
    STATUS_CHOICES = (
		('B', 'خرید'),      # Buy
		('S', "فروش"),      # Sale
	)
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="کد کالا")# کد کالا
    IdCommodity = models.ForeignKey(Commodity,on_delete=models.CASCADE,verbose_name="نام کالا")# نام کالا 
    IdStoreroom = models.ForeignKey(Storeroom,on_delete=models.CASCADE,verbose_name="نام انبار")# نام انبار )
    IdUnitofMeasurement = models.ForeignKey(UnitofMeasurement,on_delete=models.CASCADE,verbose_name="واحد سنجش")# واحد کالا 
    Count = models.IntegerField(verbose_name="تعداد")# تعداد 
    Amount = models.IntegerField(verbose_name="مبلغ جز")# مبلغ جز 
    Discount = models.IntegerField(verbose_name="تخفیف")# تخفیف 
    Taxation = models.IntegerField(verbose_name="مالیات")# مالیات 
    Date = models.DateTimeField(auto_now=True,verbose_name="تاریخ فاکتور")# تاریخ
    IdCustomer = models.ForeignKey(Customer,on_delete=models.CASCADE,verbose_name="نام مشتری")# نام مشتری
    Type = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="نوع") #نوع

    @property
    def AmountAfter(self):
        TotalAmount = self.Amount * self.Count
        DiscountAfter = (TotalAmount - (TotalAmount * (self.Discount / 100)))
        TaxationAfter = (DiscountAfter - (DiscountAfter * (self.Taxation/100)))
        return TaxationAfter

    class Meta:
        verbose_name = "فاکتور خرید/فروش"
        verbose_name_plural="فاکتورهای خرید/فروش"

    def jDate(self):
        return jalali_converter(self.Date)
    jDate.short_description = "تاریخ ثبت"

    def __str__(self):
        return self.IdCommodity.Name

class SettlementArrived(models.Model):
    STATUS_CHOICES = (
		('C', 'نقدی'),      # Cash
		('I', "قسطی"),      # Installment
	)
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="شماره سند") #شماره سند
    Type = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="نوع") #نوع
    Date = models.DateTimeField(auto_now=True,verbose_name="تاریخ سند")# تاریخ سند 
    Amount = models.IntegerField(verbose_name="مبلغ")# مبلغ
    Description = models.TextField(verbose_name="توضیحات",max_length=200)# توضیحات
    Address = models.CharField(verbose_name="آدرس",max_length=200)# آدرس
    Telephone = models.CharField(verbose_name="تلفن",max_length=10)# تلفن
    ReceiptNumber = models.CharField(max_length=20, verbose_name="شماره سند") #شماره سند
    IdStoreroom = models.ForeignKey(Storeroom,on_delete=models.CASCADE,default=29,verbose_name="نام انبار")# نام انبار )

    class Meta:
        verbose_name = "تسویه فاکتور"
        verbose_name_plural= "تسویه فاکتورها"

    def jDate(self):
        return jalali_converter(self.Date)
    jDate.short_description = "تاریخ ثبت"

    def __str__(self):
        return self.Date

class PurchaseRequest(models.Model):
    STATUS_CHOICES = (
		('Y', 'خرید شده'),
		('N', "خرید نشده"),
	)
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="شماره درخواست") #شماره درخواست
    IdCommodity = models.ForeignKey(Commodity,on_delete=models.CASCADE,verbose_name="نام کالا")# نام کالا 
    IdUnitofMeasurement = models.ForeignKey(UnitofMeasurement,on_delete=models.CASCADE,verbose_name="واحد سنجش")# واحد کالا 
    Count = models.IntegerField(verbose_name="تعداد")# تعداد 
    DateRequired = models.DateTimeField(verbose_name="تاریخ نیاز")# تاریخ نیاز
    Date = models.DateTimeField(auto_now=True,verbose_name="تاریخ ثبت")# تاریخ ثبت
    IdStoreroom = models.ForeignKey(Storeroom,on_delete=models.CASCADE,verbose_name="نام انبار")# نام انبار )
    TechnicalSpecifications = models.TextField(verbose_name="مشخصات فنی",max_length=200)# مشخصات فنی
    PurchaseSource = models.CharField(max_length=20, verbose_name="منبع خرید") #منبع خرید
    PurchasingOfficer = models.CharField(max_length=20, verbose_name="مامور خرید") #مامور خرید
    Status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت",default='N') #وضعیت

    @property
    def amount(self):
        return self.Count * self.IdCommodity.UnitPrice

    class Meta:
        verbose_name = "درخواست خرید"
        verbose_name_plural= "درخواست های خرید"

    def jDate(self):
        return jalali_converter(self.Date)
    jDate.short_description = "تاریخ ثبت"

    def jDateRequired(self):
        return jalali_converter(self.DateRequired)
    jDate.short_description = "تاریخ نیاز"

    def __str__(self):
        return self.PurchaseSource