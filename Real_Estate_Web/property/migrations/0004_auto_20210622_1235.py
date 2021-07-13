# Generated by Django 3.2.4 on 2021-06-22 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20210622_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_commercial',
            name='floor_number',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='property_commercial',
            name='personal_washrooms',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='property_commercial',
            name='total_floor',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='property_commercial',
            name='washrooms',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='property_pg',
            name='balconies',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='property_pg',
            name='bathrooms',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='property_pg',
            name='bedrooms',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='property_pg',
            name='monthly_rent',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='property_pg',
            name='security_deposit',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='property_plot',
            name='floors_allowed_for_construction',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='property_plot',
            name='number_of_openside',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='property_residential',
            name='balconies',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='property_residential',
            name='bathrooms',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='property_residential',
            name='bedrooms',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='property_residential',
            name='car_parking',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='property_residential',
            name='floor_number',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='property_residential',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='property_residential',
            name='total_floor',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
