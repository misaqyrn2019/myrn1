from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from account.models import Province,City
from django.contrib.auth import get_user_model
from extensions.utils import jalali_converter,jalali_converterWT
from FacilitiesWelfare.models import OrganizationalHouse

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