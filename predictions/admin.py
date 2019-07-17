from django.contrib import admin
from predictions.models import Prediction, Target


class TargetInline(admin.TabularInline):
    model = Target
    extra = 3

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General information', {'fields': ['title', 'coin_name', 'mcap_name', 'prediction_type', 'author']}),
        ('Description', {'fields': ['description']}),
        ('Date', {'fields': ['pub_date']}),
        ('votes', {'fields': ['votes']}),
        ('price', {'fields': ['entry', 'stop_loss']}),
        ]
    inlines = [TargetInline]
    list_display = ('title', 'coin_name', 'prediction_type', 'pub_date', 'votes', 'was_published_recently')
