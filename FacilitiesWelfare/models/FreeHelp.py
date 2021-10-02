from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from extensions.utils import jalali_converter,jalali_converterWT
import humanize

class FreeHelp(models.Model):
    TypeAssistance = (
        ('MA', "ازدواج"),
        ('BG', "هدیه تولد"),
        ('NC', "فرزند جدید"),
        ('AN', "غیره")
    )
    Id = models.AutoField(unique=True, primary_key=True, verbose_name="شناسه")
    Title = models.CharField(max_length=200, verbose_name="عنوان")
    TypeAssistance = models.CharField(max_length=2, choices=TypeAssistance, default="AN", verbose_name="نوع")
    DateRegister = models.DateTimeField(verbose_name="تاریخ ثبت")#تاریخ ثبت
    IdUser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="کاربر")
    Price = models.IntegerField(verbose_name="مبلغ")
    Description = models.TextField(verbose_name="توضیحات")

    def jDateRegister(self):
        return jalali_converterWT(self.DateRegister)
    jDateRegister.short_description = "تاریخ ثبت"

    def HPrice(self):
        return humanize.intcomma(self.Price)
    HPrice.short_description = "مبلغ"

    def __str__(self):
        self.Title

    class Meta:
        verbose_name = 'کمک بلاعوض'
        verbose_name_plural = 'کمک های بلاعوض'