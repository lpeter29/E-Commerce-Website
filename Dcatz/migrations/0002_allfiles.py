# Generated by Django 5.1.1 on 2024-11-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dcatz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=2054)),
                ('item_name', models.CharField(max_length=2054)),
                ('price', models.IntegerField()),
            ],
        ),
    ]