from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from extensions.utils import jalali_converter,jalali_converterWT

class SeeAndVisit(models.Model):#11
    Type = (
        ('F', "پدر"),
        ('M', "مادر"),
        ('P', "پدربزرگ"),
        ('Q', "مادربزرگ"),
        ('B', "برادر"),
        ('S', "خواهر"),
        ('D', "دایی"),
        ('A', "عمو"),
        ('K', "خاله"),
        ('E', "عمه"),
    )
    Id = models.AutoField(unique=True, primary_key=True, verbose_name="شناسه")
    IdUser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="شناسه کاربر")
    ConsumerItems = models.CharField(max_length=2, choices=Type, verbose_name="نسبت")
    Name = models.CharField(max_length=100, verbose_name="نام بیمار")
    Family = models.CharField(max_length=100, verbose_name="نام خانوادگی بیمار")
    DateTimeRegister = models.DateTimeField(auto_now=True,verbose_name="زمان ثبت")
    DateTimeVisit = models.DateTimeField(verbose_name="زمان عیادت")
    Description = models.TextField(verbose_name="توضیحات")

    def jDateTimeRegister(self):
        return jalali_converterWT(self.DateTimeRegister)
    jDateTimeRegister.short_description = "زمان ثبت"

    def jDateTimeVisit(self):
        return jalali_converterWT(self.DateTimeVisit)
    jDateTimeVisit.short_description = "زمان عیادت"

    def __str__(self):
        self.Name

    class Meta:
        verbose_name = "دیدن و عیادت از بیمار"
        verbose_name_plural = "دید و عیادات از بیماران"