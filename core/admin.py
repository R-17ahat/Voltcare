
from django.contrib import admin
from .models import Complaint


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):

    # INFORMATION DISPLAYED IN THE COMPLAINT LIST
    list_display = (
        'complaint_id',
        'customer',
        'category',
        'priority',
        'status',
        'created_at',
    )

    # FILTER OPTIONS
    list_filter = (
        'status',
        'priority',
        'category',
    )

    # SEARCH OPTIONS
    search_fields = (
        'complaint_id',
        'customer__username',
        'subject',
    )

    # ALLOW STATUS AND PRIORITY TO BE UPDATED
    list_editable = (
        'priority',
        'status',
    )

    # FIELDS THAT CANNOT BE EDITED
    readonly_fields = (
        'complaint_id',
        'created_at',
        'updated_at',
    )

    ordering = ('-created_at',)
