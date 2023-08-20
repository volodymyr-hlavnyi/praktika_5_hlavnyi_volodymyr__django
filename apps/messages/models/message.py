from django.db import models


class Message(models.Model):
    message_in = models.CharField(max_length=1000)
    message_out = models.CharField(max_length=1000)

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.message_in

    class Meta:
        ordering = ["-modified_at", "message_in"]
