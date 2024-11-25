from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(CartItems)
admin.site.register(AllFiles)
admin.site.register(CatAccessories)
admin.site.register(CatClothing)
admin.site.register(CatFurniture)
admin.site.register(CatFood)
admin.site.register(CatToys)

# Register your models here.
