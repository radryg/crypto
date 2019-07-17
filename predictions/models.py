import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Prediction(models.Model):
    PREDICTION_TYPES = (
        ('L', 'Long'),
        ('S', 'Short'),
    )
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    coin_name = models.SlugField(help_text='Short name of a coin')
    prediction_type = models.CharField(max_length=1, choices=PREDICTION_TYPES, null=True)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)
    entry = models.DecimalField(max_digits=10, default=0, decimal_places=8)
    stop_loss = models.DecimalField(max_digits=10, default=0, decimal_places=8)
    mcap_name = models.CharField(max_length=50, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-coin_name"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('prediction', args=[str(self.id)])

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Target(models.Model):
    prediction = models.ForeignKey(Prediction, on_delete=models.CASCADE)
    TARGET_TYPES = (
        ('P', 'Pending'),
        ('R', 'Reached'),
        ('C', 'Closed'),
    )
    target_status = models.CharField(max_length=1, choices=TARGET_TYPES, default='P')
    prediction_target = models.DecimalField(max_digits=10, default=0, decimal_places=8)

    def __str__(self):
        return str(self.prediction_target)

    class Meta:
        ordering = ["prediction_target"]


