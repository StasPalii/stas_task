from django.contrib.auth.models import User
from django.db import models


class Endpoint(models.Model):
    class Status(models.TextChoices):
        UP = 'UP', 'Up'
        DOWN = 'DOWN', 'Down'
        PENDING = 'PENDING', 'Pending'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING
    )
    # second
    time_in_between_s = models.PositiveIntegerField()

class CheckLog(models.Model):
    site = models.ForeignKey(Endpoint, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status_code = models.PositiveIntegerField()

    # millisecond
    response_time_ms = models.PositiveIntegerField(default=0)