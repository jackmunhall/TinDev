# Generated by Django 4.1.3 on 2022-12-08 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tindev', '0008_offer_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='tindev.post'),
        ),
    ]