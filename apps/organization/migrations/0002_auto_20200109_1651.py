# Generated by Django 3.0.1 on 2020-01-09 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': '城市', 'verbose_name_plural': '城市'},
        ),
        migrations.AlterModelOptions(
            name='courseorg',
            options={'verbose_name': '课程机构', 'verbose_name_plural': '课程机构'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': '教师', 'verbose_name_plural': '教师'},
        ),
    ]
