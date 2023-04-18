import os
import asyncio
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse.settings')
import django

django.setup()



# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
from admin_warehouse.models import Client, Storage, Order




def is_client_registered(tg_account: str):
    try:
        client = Client.objects.get(tg_account=tg_account)
        return client.status()
    except Client.DoesNotExist:
        return f'client with username {tg_account} is not registered'
