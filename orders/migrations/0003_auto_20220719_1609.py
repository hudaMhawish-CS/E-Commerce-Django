# Generated by Django 3.2.14 on 2022-07-19 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_order_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created_by',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='auth.user'),
            preserve_default=False,
        ),
    ]
