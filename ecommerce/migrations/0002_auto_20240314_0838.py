# Generated by Django 3.2.15 on 2024-03-14 02:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descrption',
            new_name='description',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
