import datetime
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse.settings')
import django

django.setup()

# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
from admin_warehouse.models import Client, Storage, Order, Owner
from email_validate import validate


def get_expired_orders():
    return Order.objects.filter(date_closed__lte=datetime.date.today()).exclude(is_expired=True)


def identify_user(tg_account: str):
    try:
        owner = Owner.objects.get(tg_account=tg_account)
        return 'owner'
    except Owner.DoesNotExist:
        try:
            client = Client.objects.get(tg_account=tg_account)
            return client.status()
        except Client.DoesNotExist:
            return 'Not_reg'


def registration_client(tg_account, chat_id, mail):
    Client.objects.create(tg_account=tg_account, chat_id=chat_id, mail=mail)


def check_mail(txt):
    return validate(txt)


def get_available_storages():
    return [storage for storage in Storage.objects.all() if storage.free_space() > 0]
