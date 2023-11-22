from django.contrib import admin

from contact.models import ContactRequest


@admin.register(ContactRequest)
class ContactRequestModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'name', 'request_date']
    readonly_fields = ('request_date',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
