from django.conf import settings
from django.db import models


class Pokemon(models.Model):
    """Pokemon object"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    abilities = models.CharField()
    description = models.TextField()
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)
