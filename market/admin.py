from django.contrib import admin
from market.models import Coin

class CoinAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General information', {'fields': ['coin_name', 'coinname_long', 'coin_type']}),
        ('Price information',   {'fields': ['priceBTC', 'priceUSD', 'priceETH', \
                                         'coin_tot_supply', 'coin_circ_supply', \
                                         'coin_market_cap', 'coin_daily_volume']
                                }),
        ('External information', {'fields': ['web_site', 'coin_twitter', 'coin_reddit', \
                                         'coin_source', 'coin_explorer']
                                })
        ]


admin.site.register(Coin, CoinAdmin)
