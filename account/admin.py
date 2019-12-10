from django.contrib import admin
from account.models import UserProfileInfo
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    search_fields = ['user', ]
    list_filter = ['gender', 'occupation', 'register_date', ]
    list_display = ['user', 'register_date', 'gender', 'occupation', ]


admin.site.register(UserProfileInfo, AccountAdmin)
