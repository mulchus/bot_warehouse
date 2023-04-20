# Generated by Django 4.2 on 2023-04-19 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_warehouse', '0003_order_is_expired'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_account', models.CharField(max_length=200, unique=True, verbose_name='telegram account for communication')),
                ('chat_id', models.IntegerField(blank=True, null=True, verbose_name='uniq chat_id for Bot')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='client_chat_id',
        ),
        migrations.AddField(
            model_name='client',
            name='chat_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='chat_id for Bot'),
        ),
        migrations.AddField(
            model_name='client',
            name='mail',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='e-mail address'),
        ),
    ]
