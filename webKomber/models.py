from django.db import models

# Create your models here.
class UserData(models.Model):

    class LabelAktivitas(models.IntegerChoices):
        DIAM = 0
        NAIK_MOTOR = 1
        LOMPAT_LOMPAT = 2

    nama_user = models.TextField(default='')
    label_aktivitas = models.IntegerField(
        choices=LabelAktivitas.choices,
        default=LabelAktivitas.DIAM
    )
    locations = models.JSONField()
    created_at = models.DateTimeField(auto_now=True)