# Generated by Django 3.1.7 on 2021-06-26 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20210626_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=120)),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('ordered', 'ordered'), ('despatched', 'despatched'), ('cancelled', 'cancelled')], default='ordered', max_length=10)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.addbookmodel')),
            ],
        ),
    ]
