from django.db import models
# from django.utils import timezone
# from extensions.utils import jalali_Converter
# from account.models import User,Province,City

# class Users(models.Model):
#     class Meta:
#         verbose_name = "کاربران"
#         verbose_name_plural = "کاربران"
#     Id = models.AutoField(unique=True,primary_key=True)
#     Sex = ((True,'مونث'),(False,'مذکر'))
#     Name = models.CharField(max_length=100,verbose_name="نام ")#نام
#     Family = models.CharField(max_length=100,verbose_name="نام خانوادگی ")#نام خانوادگی
#     Address = models.TextField(verbose_name="آدرس ")#آدرس
#     NationalCode = models.CharField(max_length=10,verbose_name="کد ملی ")#کدملی
#     IdNumber = models.CharField(max_length=10,verbose_name="شماره شناسنامه ")#شماره شناسنامه
#     Gender = models.BooleanField(choices=Sex,verbose_name="جنسیت ")#جنسیت
#     IdProvinceBirth = models.ForeignKey(Province,on_delete=models.CASCADE,verbose_name="نام استان ")#شناسه استان محل تولد
#     IdCityBirth = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name="نام شهرستان ")#شناسه شهرستان محل تولد
#     HomePhoneNumber = models.CharField(max_length=10,verbose_name="شماره منزل ")#شماره تماس منزل
#     MobileNumber = models.CharField(max_length=10,verbose_name="شماره همراه ")#شماره همراه
#     Email = models.EmailField(max_length=50,verbose_name="ایمیل ")#ایمیل
#     UserName = models.CharField(max_length=50,verbose_name="نام کاربری ")#نام کاربری
#     Password = models.CharField(max_length=50,verbose_name="رمز عبور ")#رمز عبور

#     def __str__(self):
#         return self.Name

# class Personnel(models.Model):
#     class Meta:
#         verbose_name = "کارکرد پرسنل"
#         verbose_name_plural = "کارکرد پرسنل"
#     Id = models.AutoField(unique=True,primary_key=True)
#     IdUsers = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name="شناسه کاربر ")#شناسه کاربر
#     PersonnelCode = models.CharField(max_length=100,verbose_name="شماره پرسنلی ")#شماره پرسنلی
#     PeriodName = models.CharField(max_length=100,verbose_name="نام شیفت ")#نام شیفت
#     OrganizationName = models.CharField(max_length=100,verbose_name="نام اداره ")#نام اداره
#     DayStatus = models.CharField(max_length=50,verbose_name="حالت روز ")#حالت روز
#     Date = models.DateTimeField(verbose_name="تاریخ ")# تاریخ
#     Login1 = models.TimeField(verbose_name="ورود 1 ")#ورود 1
#     Login2 = models.TimeField(verbose_name="ورود 2 ")#ورود 2
#     Login3 = models.TimeField(verbose_name="ورود 3 ")#ورود 3
#     Logout1 = models.TimeField(verbose_name="خروج 1 ")#خروج 1
#     Logout2 = models.TimeField(verbose_name="خروج 2 ")#خروج 2
#     Logout3 = models.TimeField(verbose_name="خروج 3 ")#خروج 3
#     TimeSpent = models.TimeField(verbose_name="کارکرد ")#کارکرد
#     LoginDelay = models.TimeField(verbose_name="تاخیر ورود ")#تاخیر ورود
#     LogoutRush = models.TimeField(verbose_name="تعجیل خروج ")#تعجیل خروج
#     WorkDeduction = models.TimeField(verbose_name="کسرکار ")#کسر کار
#     OvertimeLogin = models.TimeField(verbose_name="اضافه کار ورود ")#اضافه کار ورود
#     OvertimeLogout = models.TimeField(verbose_name="اضافه کار خروج ")#اضافه کار خروج
#     TotalOvertime = models.TimeField(verbose_name="اضافه کار کل ")#اضافه کار کل
#     Transportation = models.TimeField(verbose_name="ایاب ذهاب ")#ایاب ذهاب
#     HourlyLeave = models.TimeField(verbose_name="مرخصی ساعتی ")#مرخصی ساعتی
#     HourlyMission = models.TimeField(verbose_name="ماموریت ساعتی ")#ماموریت ساعتی
#     RoofOvertimeRemained = models.TimeField(verbose_name="مانده سقف ")#مانده سقف
    
#     # def __str__(self):
#     #     return Users.objects.filter(Id = self.Id).first().Name

#     def JDate(self):
#         return jalali_Converter(self.Date)
#     JDate.short_description = "زمان انتشار"

# class Menu(models.Model):
#     Id = models.AutoField(unique=True,primary_key=True)
#     Title = models.TextField(verbose_name="عنوان منو")

#     class Meta:
#         verbose_name = "منو"
#         verbose_name_plural="منوها"

#     def __str__(self):
#         return self.Title

# class SubMenu(models.Model):
#     Id = models.AutoField(unique=True,primary_key=True)
#     Title = models.TextField(verbose_name="عنوان منو",max_length=50)
#     HrefLink = models.TextField(verbose_name="لینک")
#     IdMenu = models.ForeignKey(Menu,on_delete=models.CASCADE,verbose_name="شناسه منو ")

#     class Meta:
#         verbose_name = "زیر منو"
#         verbose_name_plural="زیرمنوها"

#     def __str__(self):
#         return self.Title