# Generated by Django 3.2.12 on 2022-09-26 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(default=None, height_field='140px', upload_to='', width_field='100px'),
            preserve_default=False,
        ),
    ]