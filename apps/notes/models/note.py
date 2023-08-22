from django.db import models


class Note(models.Model):
    text_in = models.CharField(max_length=1000)
    text_out = models.CharField(max_length=1000)

    # passkey = models.CharField(max_length=100)

    passkey = models.ForeignKey(
        "SecretKey",
        related_name="passkey",
        on_delete=models.CASCADE,
    )

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
        return f"{self.text_out} {self.created_at} {self.modified_at}"

    class Meta:
        ordering = ["-modified_at", "text_in"]
