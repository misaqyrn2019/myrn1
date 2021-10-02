from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from account.models import Province,City
from django.contrib.auth import get_user_model
from extensions.utils import jalali_converter,jalali_converterWT

class OrganizationalHouse(models.Model):#6
    Id = models.AutoField(unique=True, primary_key=True, verbose_name="شناسه")
    Title = models.CharField(max_length=200, verbose_name="عنوان")
    IdCity = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name="شهر")
    Address = models.CharField(max_length=200, verbose_name="آدرس")
    PostalCode = models.CharField(max_length=10, verbose_name="کدپستی",default="-")
    Pelaque = models.IntegerField(default=0, verbose_name="پلاک")
    Unit = models.IntegerField(default=0, verbose_name="واحد")
    Floor = models.IntegerField(default=0, verbose_name="طبقه")
    DateRegister = models.DateTimeField(verbose_name="تاریخ ثبت")
    Description = models.TextField(verbose_name="توضیحات")

    def jDateRegister(self):
        return jalali_converterWT(self.DateRegister)
    jDateRegister.short_description = "تاریخ ثبت"

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = "خانه سازمانی"
        verbose_name_plural = "خانه های سازمانی"

class RegisterOrganizationalHouse(models.Model):
    STATUS_CHOICES = (
        ('Y', 'تایید شده'),
        ('N', "تایید نشده"),
    )
    Id = models.AutoField(unique=True, primary_key=True, verbose_name="شناسه")
    IdUser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="شناسه کاربر")
    IdOrganizationHouse = models.ForeignKey(OrganizationalHouse,on_delete=models.CASCADE,verbose_name="شناسه خانه")
    DateTimeRegister = models.DateTimeField(auto_now=True,verbose_name="زمان ثبت")
    DateExpire = models.DateTimeField(verbose_name="تاریخ انقضا")
    IsVerify = models.CharField(max_length=1, choices=STATUS_CHOICES, default="N", verbose_name="تاییدیه")

    def jDateTimeRegister(self):
        return jalali_converterWT(self.DateTimeRegister)
    jDateTimeRegister.short_description = "زمان ثبت"

    def jDateExpire(self):
        return jalali_converterWT(self.DateExpire)
    jDateExpire.short_description = "تاریخ انقضا"

    class Meta:
        verbose_name = "ثبت نام خانه سازمانی"
        verbose_name_plural = "ثبت نام خانه های سازمانی"