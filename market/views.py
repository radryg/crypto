from django.shortcuts import render, get_object_or_404
from django.views import generic
import requests
import bs4

from .models import Coin


class IndexView(generic.ListView):
    template_name = 'market/index.html'
    context_object_name = 'all_coins'

    def get_queryset(self):
        return Coin.objects.order_by('coinname_long')


class DetailView(generic.DetailView):
    model = Coin
    template_name = 'market/coin.html'
    slug_field = 'coinname_long'
    context_object_name = 'coin'


def btcprice(request, slug):
    c = get_object_or_404(Coin, coinname_long=slug)
    coin_url = 'https://coinmarketcap.com/currencies/%s' % (c.coinname_long.lower())
    get_coin = requests.get(coin_url)
    coin_site = bs4.BeautifulSoup(get_coin.text)
    selector = (coin_site.select('#quote_price > span.text-large2'))
    btcprice = selector[0].getText()
    return render(request, 'market/includes/btcprice.html', {'btcprice': btcprice})
