# Generated by Django 4.0.4 on 2022-07-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_image_admin_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='logo',
            field=models.ImageField(default='media/user.png', upload_to=''),
        ),
    ]
