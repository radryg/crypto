from django.db import models
from django.utils import timezone


class Coin(models.Model):
    COIN_TYPE = (
        ('PRIV', 'Privacy'),
        ('NETW', 'Network'),
        ('GAME', 'Gaming'),
        ('PLAT', 'Platform'),
        ('PAYM', 'Payment'),
    )
    coin_name = models.SlugField()
    coinname_long = models.SlugField()
    priceBTC = models.FloatField(max_length=10)
    priceUSD = models.FloatField(max_length=10)
    priceETH = models.FloatField(max_length=10)
    coin_type = models.CharField(max_length=50, choices=COIN_TYPE)
    web_site = models.CharField(max_length=100,  blank=True)
    coin_twitter = models.CharField(max_length=100,  blank=True)
    coin_reddit = models.CharField(max_length=100,  blank=True)
    coin_source = models.CharField(max_length=100, blank=True)
    coin_explorer = models.CharField(max_length=200, blank=True)
    coin_telegram = models.CharField(max_length=100, blank=True)
    coin_discord = models.CharField(max_length=100, blank=True)
    coin_tot_supply = models.IntegerField()
    coin_circ_supply = models.IntegerField()
    coin_market_cap = models.IntegerField()
    coin_daily_volume = models.IntegerField()

    def __str__(self):
        return self.coinname_long


