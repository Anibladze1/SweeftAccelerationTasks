from django.db import models
import uuid

from django.utils import timezone


class ShortURL(models.Model):
    full_url = models.URLField(max_length=250)
    short_url = models.CharField(max_length=8, unique=True)
    premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    times_clicked = models.IntegerField(default=0)

    def generate_short_url(self, custom=None, size=8):
        if custom:
            return custom
        else:
            unique_id = uuid.uuid4()
            short_uuid = str(unique_id)[:size]
            return short_uuid

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()
        super().save(*args, **kwargs)
