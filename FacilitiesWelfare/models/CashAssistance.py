from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from extensions.utils import jalali_converter,jalali_converterWT
import humanize

class CashAssistance(models.Model):
    TypeAssistance = (
        ('PU', "همگانی"),
        ('PR', "خاص"),
    )
    Id = models.AutoField(unique=True, primary_key=True, verbose_name="شناسه")
    Title = models.CharField(max_length=200, verbose_name="عنوان")
    TypeAssistance = models.CharField(max_length=2, choices=TypeAssistance, default="PU", verbose_name="نوع کمک")
    IdUser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="شناسه کاربر",blank=True,null=True)
    Price = models.IntegerField(verbose_name="مبلغ کمک",default=0)
    DateRegister = models.DateTimeField(verbose_name="تاریخ ثبت کمک معیشتی")#تاریخ ثبت کمک
    Description = models.TextField(verbose_name="توضیحات")

    def HPrice(self):
        return humanize.intcomma(self.Price)
    HPrice.short_description = "مبلغ"

    def jDateRegister(self):
        return jalali_converterWT(self.DateRegister)
    jDateRegister.short_description = "تاریخ ثبت کمک معیشتی"

    def __str__(self):
        self.Title

    class Meta:
        verbose_name = 'کمک معیشتی نقدی'
        verbose_name_plural = 'کمک های معیشتی'