from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, get_object_or_404
import requests
from django.db.models import F
import json
from .forms import CreatePrediction

from .models import Prediction, Target


def index_view(request):
    all_predictions = Prediction.objects.order_by('-pub_date')
    return render(request, 'predictions/index.html',
                  {'all_predictions': all_predictions})


def prediction_view(request, slug):
    prediction = get_object_or_404(Prediction, coin_name=slug)
    target = prediction.target_set.all()
    coin_url = 'https://api.coinmarketcap.com/v1/ticker/%s' \
        % (prediction.mcap_name.lower())
    response = requests.get(coin_url)
    load_coin = json.loads(response.text)
    btcprice = load_coin[0]['price_btc']
    current_rank = load_coin[0]['rank']
    price_usd = load_coin[0]['price_usd']
    daily_vol = load_coin[0]['24h_volume_usd']
    market_cap = load_coin[0]['market_cap_usd']
    available_supply = load_coin[0]['available_supply']
    total_supply = load_coin[0]['total_supply']
    max_supply = load_coin[0]['max_supply']
    change_1h = load_coin[0]['percent_change_1h']
    change_24h = load_coin[0]['percent_change_24h']
    change_7d = load_coin[0]['percent_change_7d']

    return render(
        request,
        'predictions/prediction.html',
        {'prediction': prediction, 'target': target,
         'btcprice': btcprice,
         'current_rank': current_rank,
         'price_usd': price_usd,
         'daily_vol': daily_vol,
         'market_cap': market_cap,
         'available_supply': available_supply,
         'total_supply': total_supply,
         'max_supply': max_supply,
         'change_1h': change_1h,
         'change_24h': change_24h,
         'change_7d': change_7d,
         })


def top_predictions(request):
    all_predictions = Prediction.objects.order_by('-votes')
    return render(
        request,
        'predictions/index.html',
        {'all_predictions': all_predictions},
        )


def add_prediction(request):
    if request.method == 'POST':
        prediction_form = CreatePrediction(request.POST)
        if prediction_form.is_valid():
            csrf_token = django.middleware.csrf.get_token(request)
            prediction_title = form.cleaned_data['title']
            prediction_coin_name = form.cleaned_data['coin_name']
            prediction_prediction_type = form.cleaned_data['prediction_type']
            prediction_description = form.cleaned_data['description']
            prediction_entry = form.cleaned_data['entry']
            prediction_stop_loss = form.cleaned_data['stop_loss']
            # prediction_target = form.cleaned_data['target']
            # prediction_target2 = form.cleaned_data['target2']
            # prediction_target3 = form.cleaned_data['target3']
            prediction_user = request.user
            new_prediction = Prediction(
                title=prediction_title,
                coin_name=prediction_coin_name,
                prediction_prediction_type=prediction_type,
                description=prediction_description,
                entry=prediction_entry,
                stop_loss=prediction_stop_loss,
                # prediction_target=prediction_target,
                # prediction_target=prediction_target2,
                # prediction_target=prediction_target3,
                )
            new_prediction.save()
            return render(request, 'predictions/add_prediction.html', {})
    else:
        prediction_form = CreatePrediction()
    return render(request, 'predictions/add_prediction.html',
                  {'prediction_form': prediction_form})


# def vote(request, slug):
#     Prediction.objects.filter(id__in=statements).update(votes=F('votes') + 1)
#     prediction = get_object_or_404(Prediction, coin_name=slug)
#     prediction.votes += 1
#     prediction.save()
#     return HttpResponseRedirect('predictions:prediction')
