# Generated by Django 5.0 on 2023-12-27 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pratas', '0003_alter_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
