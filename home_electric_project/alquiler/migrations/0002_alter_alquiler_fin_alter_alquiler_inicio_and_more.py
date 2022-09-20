# Generated by Django 4.1 on 2022-09-17 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alquiler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquiler',
            name='fin',
            field=models.DateField(default='2022-01-01'),
        ),
        migrations.AlterField(
            model_name='alquiler',
            name='inicio',
            field=models.DateField(default='2022-01-01'),
        ),
        migrations.AlterField(
            model_name='alquiler',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]