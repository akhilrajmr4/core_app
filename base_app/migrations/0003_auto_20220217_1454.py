# Generated by Django 3.0.14 on 2022-02-17 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_auto_20220217_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extracurricular',
            name='projecturl',
            field=models.CharField(blank=True, default='', max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='extracurricular',
            name='skill1',
            field=models.CharField(blank=True, default='', max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='extracurricular',
            name='skill2',
            field=models.CharField(blank=True, default='', max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='extracurricular',
            name='skill3',
            field=models.CharField(blank=True, default='', max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='extracurricular',
            name='status',
            field=models.CharField(default='', max_length=240),
        ),
    ]
