# Generated by Django 3.2.6 on 2022-05-25 15:24

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
                ('product_name', models.CharField(default='', max_length=50)),
                ('catagory', models.CharField(default='', max_length=50)),
                ('subcatagory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('descricption', models.CharField(default='', max_length=250)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('image', models.ImageField(default='', upload_to='FASHION/images')),
                ('product_qty', models.IntegerField(default=0)),
            ],
        ),
    ]
