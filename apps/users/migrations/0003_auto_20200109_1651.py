# Generated by Django 3.0.1 on 2020-01-09 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_banner_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '轮播图', 'verbose_name_plural': '轮播图'},
        ),
        migrations.AlterModelOptions(
            name='emailverifyrecord',
            options={'verbose_name': '邮箱验证码', 'verbose_name_plural': '邮箱验证码'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=7, verbose_name='性别'),
        ),
    ]
