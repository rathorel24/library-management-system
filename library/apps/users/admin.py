from django.contrib import admin
from apps.users.models import User, UserManager
from django.contrib.auth.models import Group

# admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ["email"]
    fields = ('email','first_name','last_name','role','is_staff','is_superuser','is_active','password')
    readonly_fields = ('created_at','modified_at','password')

