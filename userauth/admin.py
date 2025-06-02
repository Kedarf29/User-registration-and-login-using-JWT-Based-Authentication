
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rangefilter.filters import DateRangeFilter
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser



class CustomUserAdmin(ImportExportModelAdmin, UserAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm

    model = CustomUser

    list_display = ('email','username', 'first_name', 'last_name', 'is_staff', 'is_active_status','date_joined')
    list_filter = ('is_staff', 'is_active', ('date_joined', DateRangeFilter))
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    date_hierarchy = 'date_joined'

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')},
        ),
    )

    def is_active_status(self, obj):
        return "✅ Active" if obj.is_active else "❌ Inactive"
    is_active_status.short_description = "Status"

    def get_readonly_fields(self, request, obj=None):
        if obj and request.user.is_superuser:
            return self.readonly_fields + ('email',)
        return self.readonly_fields


admin.site.register(CustomUser, CustomUserAdmin)
