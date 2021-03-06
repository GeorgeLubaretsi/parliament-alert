from django.db import models
from apps.categories.models import Category
from rapidsms.models import Contact

# Create your models here.
# Store every alert that we send about Parliament
class ParliamentAlert(models.Model):
    categories = models.ManyToManyField(Category,null=False)
    text_en = models.CharField(max_length=150)
    text_ka = models.CharField(max_length=150)
    create_date = models.DateField(auto_now_add=True)

#    LANG_CHOICES = (
#            ('en', 'English'),
#            ('ka', 'Georgian'),
#            )
#    language = models.CharField(max_length=2,choices=LANG_CHOICES)
    # Subscribers default to receive only the most important alerts
    is_important = models.BooleanField(default=False)
    sent = models.BooleanField(default=False,editable=False)
    sent_date = models.DateField(null=True,editable=False)

    def __unicode__(self):
        return self.text_en[:20]

# Track every attempt at sending a message.
# This may become unwieldy if the service becomes
# popular, but for now, it will be valuable to be
# able to see this data.
class AlertSendAttempt(models.Model):
    contact = models.ForeignKey(Contact)
    alert = models.ForeignKey(ParliamentAlert)
    date = models.DateField(auto_now_add=True)
    success = models.BooleanField()
