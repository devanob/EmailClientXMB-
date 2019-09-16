from django.urls import reverse
from django.db.models import TextField
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models as models

##define model here
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import EmailField
from django.db.models import TextField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Email(models.Model):

    # Fields
    message = models.TextField(max_length=1000)
    subject = models.CharField(max_length=50)
    date = models.DateTimeField()
    fromEmail = models.EmailField()
    toEmail = models.EmailField()
    isArchived = models.BooleanField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('Email_email_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('Email_email_update', args=(self.pk,))

  



