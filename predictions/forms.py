from django.forms import ModelForm
from django.db import models
from .models import Prediction

class CreatePrediction(ModelForm):
    class Meta:
        model = Prediction
        fields = '__all__'#['title', 'coin_name', 'prediction_type', 'description', 'entry', 'stop_loss', 'target']

       # prediction_target = models.DecimalField(max_digits=10, default=0, decimal_places=8)
        # prediction_target = models.DecimalField(max_digits=10, default=0, decimal_places=8)
