# Generated by Django 3.1.7 on 2021-06-26 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addbookmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_name', models.CharField(max_length=120)),
                ('Author', models.CharField(max_length=120)),
                ('Price', models.IntegerField()),
                ('img', models.ImageField(upload_to='images')),
            ],
        ),
    ]
