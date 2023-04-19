import datetime
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver


class Owner(models.Model):
    tg_account = models.CharField('telegram account for communication', max_length=200, unique=True)
    chat_id = models.IntegerField('uniq chat_id for Bot', null=True, blank=True)

    def __str__(self):
        return f'owner {self.tg_account}'


class Client(models.Model):
    tg_account = models.CharField('telegram account for communication', max_length=200, unique=True)
    chat_id = models.IntegerField('chat_id for Bot', null=True, blank=True)
    mail = models.CharField('e-mail address', max_length=200, null=True, blank=True)

    def status(self):
        active_orders = Order.objects.filter(client=self, date_closed__gte=datetime.date.today(),
                                             date_opened__lte=datetime.date.today()).count()
        return active_orders

    def __str__(self):
        return self.tg_account


class Storage(models.Model):
    address = models.CharField('address of storage', max_length=300)
    area = models.FloatField('whole area of storage')

    def free_space(self):
        taken_area = Order.objects.filter(storage=self).aggregate(Sum('area'))['area__sum']
        if taken_area:
            return self.area - taken_area
        return self.area

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, verbose_name='client', related_name='orders',
                               null=True)
    storage = models.ForeignKey(Storage, on_delete=models.SET_NULL, verbose_name='storage', related_name='orders',
                                null=True, blank=True)
    area = models.FloatField('whole area of storage')
    date_opened = models.DateField(verbose_name='date of opening the order', null=True, blank=True)
    date_closed = models.DateField(verbose_name='date of closing the order', null=True, blank=True)
    is_expired = models.BooleanField(verbose_name='area was cleared', null=True, blank=True)

    def __str__(self):
        if self.client:
            return f'{self.client.tg_account}_{self.id}'
        else:
            return f'No_client_{self.id}'


@receiver(post_save, sender=Order)
def order_changed(sender, instance, **kwargs):
    """ client have cleared area"""
    if instance.is_expired:
        Order.objects.filter(id=instance.id).update(area=0)
