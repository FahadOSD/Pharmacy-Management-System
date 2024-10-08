# Generated by Django 5.0.6 on 2024-09-05 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('drug', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('buyer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.accounts')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('drug_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drug.drug')),
            ],
        ),
    ]
