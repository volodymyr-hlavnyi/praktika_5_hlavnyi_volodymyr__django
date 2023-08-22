from apps.notes.models import Note, SecretKey
from apps.services.secret import get_encrypt_decrypt_string


def create_object_note(text_in: str, passkey_pk: int) -> Note:
    text_in = text_in
    passkey = SecretKey.objects.filter(pk=passkey_pk).first()
    text_out = get_encrypt_decrypt_string(text_in, passkey.value, mode="encrypt", debug=False)
    return Note(
        text_in=text_in,
        passkey=passkey,
        text_out=text_out,
    )


def save_note(text_in: str, passkey_pk: int) -> None:
    # logger = logging.getLogger("django")

    # queryset = GameWord.objects.all()

    # logger.info(f"Current amount of words before: {queryset.count()}")

    note_secret = create_object_note(text_in=text_in, passkey_pk=passkey_pk)
    note_secret.save()

    # logger.info(f"Current amount of words after: {queryset.count()}")
