from django.contrib import admin
from accounts.models import *

# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
	fields = ('username','first_name','last_name', 'password','gender','birthday','address','facebook','twitter')
	list_display = ('first_name','last_name')


admin.site.register(UserAccount,UserAccountAdmin)