# Generated by Django 3.1.2 on 2020-10-13 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InspectionRecords',
            fields=[
                ('restaurant_Inspection_ID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('restaurant_name', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=200)),
                ('business_address', models.CharField(max_length=200)),
                ('is_roadway_compliant', models.CharField(max_length=200)),
                ('skipped_reason', models.CharField(max_length=200)),
                ('inspected_on', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=200)),
                ('business_address', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=200)),
                ('business_id', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('legal_business_name', models.CharField(default=None, max_length=200)),
            ],
            options={
                'unique_together': {('restaurant_name', 'business_address', 'postcode')},
            },
        ),
    ]