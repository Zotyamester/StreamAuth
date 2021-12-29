from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.crypto import get_random_string


class Stream(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE)
    key = models.CharField(max_length=64, blank=True, unique=True,
                           validators=[MinLengthValidator(64)])
    live_at = models.DateTimeField(blank=True, null=True)

    def generate_key(self):
        key = get_random_string(64)
        while Stream.objects.filter(key=key):
            key = get_random_string(64)
        self.key = key

    def save(self, *args, **kwargs):
        if not self.key:
            self.generate_key()
        super(Stream, self).save(*args, **kwargs)
