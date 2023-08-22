from django import forms

from apps.notes.models import Note, SecretKey


class NoteForm(forms.Form):
    text_in = forms.CharField(
        label="Text (in)",
        required=True,
    )

    passkey = forms.ModelChoiceField(
        queryset=SecretKey.objects.all(),
        label="passkey",
        required=True,
    )

    class Meta:
        model = Note

        fieldsets = ("text_in", "passkey")


class NoteSecretForm(forms.ModelForm):
    # text_in = forms.CharField(
    #     label="Text (in)",
    #     required=True,
    # )
    #
    # passkey = forms.ModelChoiceField(
    #     queryset=SecretKey.objects.all(),
    #     label="passkey",
    #     required=True,
    # )

    class Meta:
        model = Note

        fields = ("text_in", "passkey")
