import datetime
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse.settings')
import django

django.setup()

# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
from admin_warehouse.models import Client, Storage, Order, Owner
from django.db.models import F
from email_validate import validate


def get_expired_orders():
    orders = Order.objects.filter(date_closed__lt=datetime.date.today()).exclude(is_expired=True)
    ord = []
    for order in orders:
        expired_orderes = {
            'order': order,
            'chat_id': order.client.chat_id,
            'client': order.client,
            'storage': order.storage,
            'expired days': -(order.date_closed - datetime.date.today()).days
        }
        ord.append(expired_orderes)
    return ord


def get_terms_orders3():
    orders = Order.objects.filter(date_closed__gte=datetime.date.today(), date_closed__lte=datetime.date.today()+datetime.timedelta(days=30)).exclude(is_expired=True)
    ord = []
    for order in orders:
        expired_orderes = {
            'order': order,
            'chat_id': order.client.chat_id,
            'client': order.client,
            'storage': order.storage,
            'expired days': -(order.date_closed - datetime.date.today()).days
        }
        ord.append(expired_orderes)
    return ord

def get_terms_orders1():
    orders = Order.objects.filter(0<F('date_closed') - datetime.date.today()<30).exclude(is_expired=True)
    ord = []
    for order in orders:
        expired_orderes = {
            'order': order,
            'chat_id': order.client.chat_id,
            'client': order.client,
            'storage': order.storage,
            'expired days': -(order.date_closed - datetime.date.today()).days
        }
        ord.append(expired_orderes)
    return ord


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
