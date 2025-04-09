from django.contrib import admin
from .models import Items
# Register your models here.

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meals","status")
    list_filter = ("status",)
    search_fields = ("meals","meals_description")


admin.site.register(Items,MenuItemAdmin)
