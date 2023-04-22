import datetime
import os
from aiogram import types

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warehouse.settings')
import django

django.setup()

from admin_warehouse.models import Client, Storage, Order, Owner, Cost
from email_validate import validate


def get_terms_orders():
    orders30 = Order.objects.filter(date_closed=datetime.date.today() + datetime.timedelta(days=30)).exclude(
        is_expired=True)
    orders14 = Order.objects.filter(date_closed=datetime.date.today() + datetime.timedelta(days=14)).exclude(
        is_expired=True)
    orders3 = Order.objects.filter(date_closed=datetime.date.today() + datetime.timedelta(days=3)).exclude(
        is_expired=True)
    orders00 = Order.objects.filter(date_closed__lt=datetime.date.today()).exclude(is_expired=True)
    ord = [[], [], [], []]
    orders_terms = [orders30, orders14, orders3, orders00]
    for orders in orders_terms:
        for order in orders:
            expired_orderes = {
                'order': order,
                'chat_id': order.client.chat_id,
                'client': order.client,
                'storage': order.storage,
                'expired days': -(order.date_closed - datetime.date.today()).days
            }
            ord[orders_terms.index(orders)].append(expired_orderes)
    return ord[0], ord[1], ord[2], ord[3]


def identify_user(tg_account: str):
    try:
        owner = Owner.objects.get(tg_account=tg_account)
        return 'owner'
    except Owner.DoesNotExist:
        try:
            client = Client.objects.get(tg_account=tg_account)
            return client.status()
        except Client.DoesNotExist:
            return 'User is not registered'


def registration_client(tg_account, chat_id, mail):
    Client.objects.create(tg_account=tg_account, chat_id=chat_id, mail=mail)


def check_mail(txt):
    return validate(txt)


def get_available_storages():
    return [storage for storage in Storage.objects.all() if storage.free_space() > 0]


def get_cost_field(field):
    instance = Cost.objects.first()
    cost_field = dict(metr_0_3=instance.metr_0_3, metr_3_7=instance.metr_3_7, metr_7_10=instance.metr_7_10,
                      metr_10=instance.metr_10, mass_0_10=instance.mass_0_10, mass_10_25=instance.mass_10_25,
                      mass_25_40=instance.mass_25_40, mass_40_70=instance.mass_40_70, mass_70_100=instance.mass_70_100,
                      mass_100=instance.mass_100)
    return cost_field[field]


def make_order(mass=None, sq=None, period=None, amount=None, tg_account=None):
    client = Client.objects.get(tg_account=tg_account)
    date_opened = datetime.date.today()
    date_closed = date_opened + datetime.timedelta(days=period)
    Order.objects.create(client=client, area=sq, mass=mass, is_expired=False, date_opened=date_opened,
                         date_closed=date_closed, amount=amount)


def get_orders(tg_account):
    client = Client.objects.get(tg_account=tg_account)
    orders = Order.objects.filter(client=client)
    serialized_orders = []
    for order in orders:
        serialized_order = dict(client=tg_account, area=order.area, mass=order.mass,
                                amount=order.amount, date_opened=order.date_opened, date_closed=order.date_closed,
                                id=order.id)
        serialized_orders.append(serialized_order)
    return serialized_orders


def delete_order(id):
    Order.objects.get(id=id).delete()

def get_qr():
    return 'FORTUNA NON PENIS, IN MANUS NON RECIPI'
