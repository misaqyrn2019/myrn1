from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,City,Province

class CityAdmin(admin.ModelAdmin):
    list_display = ('Id','Name','IdProvince')

class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('Id','Name')

UserAdmin.fieldsets[2][1]['fields'] = (
										'is_active',
										'is_staff',
										'is_superuser',
										'is_author',
										'is_storekeeper',
										'special_user',
										'groups',
										'user_permissions',
									)

UserAdmin.list_display += ('is_author', 'is_special_user','is_storekeeper')

admin.site.register(User, UserAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Province, ProvinceAdmin)