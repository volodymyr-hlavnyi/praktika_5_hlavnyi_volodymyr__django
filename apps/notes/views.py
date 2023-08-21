from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from apps.notes.models import Note, SecretKey


class NotesListView(ListView):
    model = Note


class SecretKeyListView(ListView):
    model = SecretKey


class NoteCreateView(CreateView):
    model = Note
    fields = ["text_in", "passkey"]
    success_url = reverse_lazy("notes:notes_list")


class SecretKeyCreateView(CreateView):
    model = SecretKey
    fields = ["value"]
    success_url = reverse_lazy("notes:notes_list")


class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy("notes:notes_list")


class SecretKeyDeleteView(DeleteView):
    model = SecretKey
    success_url = reverse_lazy("notes:secretkey_list")


class NoteEditView(UpdateView):
    model = Note
    fields = (
        "text_in",
        "passkey",
    )

    def get_success_url(self):
        # return reverse_lazy("contacts:contacts_update", kwargs=dict(pk=self.kwargs["pk"]))
        return reverse_lazy("notes:notes_list")


class SecretKeyEditView(UpdateView):
    model = SecretKey
    fields = ("value",)

    def get_success_url(self):
        # return reverse_lazy("contacts:contacts_update", kwargs=dict(pk=self.kwargs["pk"]))
        return reverse_lazy("notes:secretkey_list")
