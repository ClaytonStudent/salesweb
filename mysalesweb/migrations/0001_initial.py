# Generated by Django 4.0.6 on 2024-04-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('barcodes', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('sku', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('location', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('unit', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('note', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]