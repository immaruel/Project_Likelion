# Generated by Django 3.0.7 on 2020-08-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200814_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('한식', '한식'), ('퓨전', '퓨전'), ('서양', '퓨전'), ('일본', '일본'), ('이탈리아', '이탈리아'), ('동남아시아', '동남아시아')], max_length=200, null=True),
        ),
    ]