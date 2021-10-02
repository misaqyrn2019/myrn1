from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from extensions.utils import jalali_converter,jalali_converterWT
import humanize

class ConsumerItems(models.Model):
    TypeAssistance = (
        ('F', "رایگان"),
        ('C', "نقدی"),
    )
    Id = models.AutoField(unique=True, primary_key=True, verbose_name="شناسه")
    Title = models.CharField(max_length=200, verbose_name="عنوان")
    TypeAssistance = models.CharField(max_length=1, choices=TypeAssistance, default="F", verbose_name="نوع")
    Items = models.CharField(max_length=500,verbose_name="اقلام")
    Price = models.IntegerField(verbose_name="مبلغ")
    DateRegister = models.DateTimeField(verbose_name="تاریخ ثبت")#تاریخ ثبت
    DateExpire = models.DateTimeField(verbose_name="تاریخ انقضا")#تاریخ انقضا
    Description = models.TextField(verbose_name="توضیحات")

    def HPrice(self):
        return humanize.intcomma(self.Price)
    HPrice.short_description = "مبلغ"

    def jDateRegister(self):
        return jalali_converterWT(self.DateRegister)
    jDateRegister.short_description = "تاریخ ثبت"

    def jDateExpire(self):
        return jalali_converterWT(self.DateExpire)
    jDateExpire.short_description = "تاریخ انقضا"

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'قلم مصرفی'
        verbose_name_plural = 'اصلام مصرفی'

class ConsumerItemsRegister(models.Model):
    ACT = (
        ('Y', "تحویل شده"),
        ('N', "تحویل نشده"),
    )
    Id = models.AutoField(unique=True, primary_key=True, verbose_name="شناسه")
    IdConsumerItems = models.ForeignKey(ConsumerItems,on_delete=models.CASCADE,verbose_name="قلم مصرفی")
    IdUser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="شناسه کاربر")
    DateRegister = models.DateTimeField(auto_now=True,verbose_name="تاریخ ثبت")#تاریخ ثبت
    IsReceived = models.CharField(max_length=1, choices=ACT, default="N", verbose_name="تحویل شده")

    def jDateRegister(self):
        return jalali_converterWT(self.DateRegister)
    jDateRegister.short_description = "تاریخ ثبت"

    def __str__(self):
        return self.Id

    class Meta:
        verbose_name = 'ثبت نام قلم مصرفی'
        verbose_name_plural = 'ثبت نام اقلام مصرفی'