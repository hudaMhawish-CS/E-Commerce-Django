# Generated by Django 3.2.14 on 2022-07-04 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATName', models.CharField(db_index=True, max_length=50, verbose_name='name')),
                ('CATSlug', models.SlugField(unique=True, verbose_name='Category URL')),
                ('CATDesc', models.TextField(verbose_name='description')),
                ('CATImage', models.ImageField(upload_to='category/', verbose_name='Image')),
                ('CATParent', models.ForeignKey(blank=True, limit_choices_to={'CATParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='myapp.category', verbose_name='Main category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDName', models.CharField(db_index=True, max_length=200, verbose_name='Product Name')),
                ('PRDImage', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Image')),
                ('PRDDesc', models.TextField(verbose_name='Description')),
                ('PRDPrice', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('PRDStock', models.PositiveIntegerField(verbose_name='stock')),
                ('PRDDiscountPrice', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Discount Price')),
                ('PRDCost', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cost')),
                ('PRDCreated', models.DateTimeField(verbose_name='Created At')),
                ('PRDSlug', models.SlugField(unique=True, verbose_name='Product URL')),
                ('PRDIsNew', models.BooleanField(default=True, verbose_name='New Product')),
                ('PRDBestSeller', models.BooleanField(default=False, verbose_name='Best Seller')),
                ('PRDBrand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand', verbose_name='Image')),
                ('PRDCategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='myapp.category', verbose_name='Category')),
                ('PRDparent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='myapp.product')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDIImage', models.ImageField(upload_to='product/', verbose_name='Image')),
                ('PRDIProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product', verbose_name='Product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Alternative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PALNAlternative', models.ManyToManyField(related_name='alternative_products', to='myapp.Product', verbose_name='Alternatives')),
                ('PALNProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_products', to='myapp.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product Alternative',
                'verbose_name_plural': 'Product Alternatives',
            },
        ),
        migrations.CreateModel(
            name='Product_Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PACCAlternative', models.ManyToManyField(related_name='accessories_products', to='myapp.Product', verbose_name='Accessories')),
                ('PACCProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainAccessory_products', to='myapp.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product Accessory',
                'verbose_name_plural': 'Product Accessories',
            },
        ),
    ]
