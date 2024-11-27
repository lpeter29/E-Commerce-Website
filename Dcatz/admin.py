from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

class AllFilesAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.file_image:  # Replace `file_image` with your actual ImageField name
            return mark_safe(f'<img src="{obj.file_image.url}" style="width: 50px; height: 50px;" />')
        return "No Image"
    image_tag.short_description = 'AllFiles'
    list_display = ['item_name', 'price', 'description', 'image_tag',]

class CatProductsAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'price', 'file_name',]

class VarietyCatProductsAdmin(admin.ModelAdmin):
    list_display = ['variety_name', 'variety', 'variety_image',]

admin.site.register(UserProfile)
admin.site.register(CartItems)
admin.site.register(AllFiles, AllFilesAdmin)
admin.site.register(CatAccessories, CatProductsAdmin)
admin.site.register(CatClothing, CatProductsAdmin)
admin.site.register(CatFurniture, CatProductsAdmin)
admin.site.register(CatFood, CatProductsAdmin)
admin.site.register(CatToys, CatProductsAdmin)
admin.site.register(varieties, VarietyCatProductsAdmin)

# Register your models here.
