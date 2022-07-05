from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    CATName = models.CharField(max_length=50, verbose_name=_("name"),db_index=True)
    CATSlug = models.SlugField(max_length=50, verbose_name=_("Category URL"),unique=True,db_index=True)
    CATParent = models.ForeignKey('self',related_name='children',limit_choices_to={'CATParent__isnull': True},on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Main category"))
    CATDesc = models.TextField(verbose_name=_("description"))
    CATImage = models.ImageField(upload_to='category/', verbose_name=_("Image"))


    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.CATName

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.CATSlug})


class Product(models.Model):
    PRDName = models.CharField(max_length=200, verbose_name=_("Product Name"),db_index=True)
    PRDparent = models.ForeignKey('self', related_name='variants', on_delete=models.CASCADE, blank=True, null=True)
    PRDCategory = models.ForeignKey('Category', related_name='products',on_delete=models.CASCADE,blank=True,null=True, verbose_name=_("Category"))
    PRDImage = models.ImageField(upload_to='product/',verbose_name=_("Image"),blank=True,null=True)
    PRDBrand = models.ForeignKey('settings.Brand',on_delete=models.CASCADE,blank=True,null=True, verbose_name=_("Image"))
    PRDDesc = models.TextField(verbose_name=_("Description"))
    PRDPrice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Price"))
    PRDStock = models.PositiveIntegerField( verbose_name=_("stock"))
    PRDDiscountPrice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Discount Price"))
    PRDCost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Cost"))
    PRDCreated = models.DateTimeField( verbose_name=_("Created At"))

    PRDSlug = models.SlugField(max_length=50, verbose_name=_("Product URL"),unique=True,db_index=True)
    PRDIsNew = models.BooleanField(default=True, verbose_name=_("New Product"))
    PRDBestSeller = models.BooleanField(default=False, verbose_name=_("Best Seller"))

    def save(self, *args, **kwargs):
        if not self.PRDSlug:
            self.PRDSlug = slugify(self.PRDName)
        super(Product,self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return reverse('product_detail',kwargs={'slug':self.PRDSlug})

    def __str__(self):
        return self.PRDName


class ProductImage(models.Model):
    PRDIProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    PRDIImage = models.ImageField(upload_to='product/',verbose_name=_("Image"))

    def __str__(self):
        return str(self.PRDIProduct)



class Product_Alternative(models.Model):
    PALNProduct = models.ForeignKey(Product, related_name='main_products',on_delete=models.CASCADE, verbose_name=_("Product"))
    PALNAlternative = models.ManyToManyField(Product, related_name='alternative_products', verbose_name=_("Alternatives"))

    class Meta:
        verbose_name = _("Product Alternative")
        verbose_name_plural = _("Product Alternatives")

    def __str__(self):
        return str(self.PALNProduct)

class Product_Accessories(models.Model):
    PACCProduct = models.ForeignKey(Product, related_name='mainAccessory_products',on_delete=models.CASCADE, verbose_name=_("Product"))
    PACCAlternative = models.ManyToManyField(Product, related_name='accessories_products', verbose_name=_("Accessories"))

    class Meta:
        verbose_name = _("Product Accessory")
        verbose_name_plural = _("Product Accessories")

    def __str__(self):
        return str(self.PACCProduct)




