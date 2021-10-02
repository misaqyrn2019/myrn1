from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from account.models import Province,City
from django.contrib.auth import get_user_model
from extensions.utils import jalali_converter,jalali_converterWT

class TypeProject(models.Model):
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="شناسه نوع")
    Name = models.CharField(max_length=200,verbose_name="عنوان")
    
    class Meta:
        verbose_name = "نوع پروژه"
        verbose_name_plural = "انواع پروژه"

    def __str__(self):
        return self.Name

class Project(models.Model):
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="شناسه")
    Name = models.CharField(max_length=200,verbose_name="عنوان پروژه")
    RegisterDateTime = models.DateTimeField(auto_now=True)#تاریخ ثبت پروژه
    IdTypeProject = models.ForeignKey(TypeProject,on_delete=models.CASCADE,verbose_name= "نوع پروژه")#نوع پروژه
    Description = models.TextField(verbose_name="توضیحات")
    IdCity = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name= "شهر")#شهر
    Address = models.CharField(max_length=200,verbose_name="آدرس")#آدرس    

    def jRegisterDateTime(self):
        return jalali_converterWT(self.RegisterDateTime)
    jRegisterDateTime.short_description = "تاریخ ثبت"

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه ها"

    def __str__(self):
        return self.Name

class RegisterProject(models.Model):
    Id = models.AutoField(unique=True,primary_key=True,verbose_name="شناسه")
    RegisterDateTime = models.DateTimeField(auto_now=True,verbose_name="تاریخ ثبت")#تاریخ ثبت
    IdUser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,verbose_name= "کاربر")
    IdProject = models.ForeignKey(Project, on_delete=models.CASCADE,verbose_name= "پروژه")

    def jRegisterDateTime(self):
        return jalali_converterWT(self.RegisterDateTime)
    jRegisterDateTime.short_description = "تاریخ ثبت"

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه ها"

    def __str__(self):
        return self.IdProject.Name