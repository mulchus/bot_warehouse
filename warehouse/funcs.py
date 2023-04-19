import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse.settings')
import django

django.setup()

# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
from admin_warehouse.models import Client, Storage, Order, Owner
from email_validate import validate


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