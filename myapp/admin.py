from django.contrib import admin
from  .models import Product, ProductImage,Category,Product_Alternative
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('CATName','CATSlug',)
    prepopulated_fields = {'CATSlug':('CATName',)}


admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('PRDName','PRDSlug','PRDCategory','PRDPrice','PRDStock','PRDCost','PRDDiscountPrice','PRDCreated',)
    list_filter = ('PRDCategory','PRDCreated',)
    list_editable = ('PRDPrice','PRDStock',)
    prepopulated_fields = {'PRDSlug':('PRDName',)}


admin.site.register(Product,ProductAdmin)

admin.site.register(ProductImage)
admin.site.register(Product_Alternative)