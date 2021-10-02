from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from account.models import Province,City
from extensions.utils import jalali_converter,jalali_converterWT
from django.contrib.auth import get_user_model
import humanize

class Reward(models.Model):
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="شناسه")
    Title = models.CharField(max_length=200,verbose_name="عنوان پاداش")
    AssignmentDate = models.DateTimeField(verbose_name="تاریخ واگذاری")
    Price = models.IntegerField(verbose_name="مبلغ پاداش")
    Description = models.TextField(verbose_name="توضیحات")
    IdUser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,verbose_name= "کاربر")

    def jAssignmentDate(self):
        return jalali_converterWT(self.AssignmentDate)
    jAssignmentDate.short_description = "تاریخ واگذاری"

    def HPrice(self):
        return humanize.intcomma(self.Price)
    HPrice.short_description = "مبلغ"

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'پاداش'
        verbose_name_plural = 'پاداش ها'