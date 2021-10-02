from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Province(models.Model):
    class Meta:
        verbose_name = "استان"
        verbose_name_plural = "استان"
    Id = models.AutoField(unique=True,primary_key=True)
    Name = models.CharField(max_length=200,verbose_name="نام استان ")#نام استان

    def __str__(self):
        return self.Name

class City(models.Model):
    class Meta:
        verbose_name = "شهرستان"
        verbose_name_plural = "شهرستان"
    Id = models.AutoField(unique=True,primary_key=True)
    Name = models.CharField(max_length=200,verbose_name="نام شهرستان ")#نام شهرستان
    IdProvince = models.ForeignKey(Province,on_delete=models.CASCADE,verbose_name= "نام استان ",default=1)#شناسه استان
	
    def __str__(self):
        return self.Name

class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='ایمیل')

    is_author = models.BooleanField(default=False, verbose_name="مدیر نویسنده")
    special_user = models.DateTimeField(default=timezone.now, verbose_name="کاربر ویژه تا")

    is_storekeeper = models.BooleanField(default=False, verbose_name="مدیر انباردار")
    storekeeper_user = models.DateTimeField(default=timezone.now, verbose_name="کاربر انباردار تا")
    
    is_FacilitiesWelfare = models.BooleanField(default=False, verbose_name="مدیر بخش امورات رفاهی")
    FacilitiesWelfare_user = models.DateTimeField(default=timezone.now, verbose_name="کاربر امور رفاهی تا")

    Bnk_CardNumber = models.CharField(max_length=100,verbose_name="شماره کارت",default="-")
    Bnk_Shaba = models.CharField(max_length=100,verbose_name="شماره شبا",default="-")

    def is_FacilitiesWelfare_user(self):
        if self.FacilitiesWelfare_user > timezone.now():
            return True
        else:
            return False
    is_FacilitiesWelfare_user.boolean = True
    is_FacilitiesWelfare_user.short_description = "وضعیت امور رفاهی تا"

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    is_special_user.boolean = True
    is_special_user.short_description = "وضعیت کاربر ویژه"

    def is_storekeeper_user(self):
        if self.storekeeper > timezone.now():
            return True
        else:
            return False
    is_storekeeper.boolean = True
    is_storekeeper.short_description = "وضعیت انباردار تا"

    IdCity = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name="نام شهرستان",default=1)