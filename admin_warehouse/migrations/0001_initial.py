# Generated by Django 4.2 on 2023-04-17 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_account', models.CharField(max_length=200, unique=True, verbose_name='telegram account for communication')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300, verbose_name='address of storage')),
                ('area', models.IntegerField(verbose_name='whole area of storage')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.IntegerField(verbose_name='whole area of storage')),
                ('date_opened', models.DateField(blank=True, null=True, verbose_name='date of opening the order by client')),
                ('date_closed', models.DateField(blank=True, null=True, verbose_name='date of closing the order by client')),
                ('client_chat_id', models.IntegerField(blank=True, null=True, verbose_name='chat id to send messages to client')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='admin_warehouse.client', verbose_name='client')),
                ('storage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='admin_warehouse.storage', verbose_name='storage')),
            ],
        ),
    ]
