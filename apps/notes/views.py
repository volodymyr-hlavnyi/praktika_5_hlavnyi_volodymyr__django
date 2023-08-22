from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, FormView
from django.shortcuts import render

from apps.notes.forms import NoteForm, NoteSecretForm
from apps.notes.models import Note, SecretKey
from apps.services.save_note import save_note
from apps.services.secret import get_encrypt_decrypt_string


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
    success_url = reverse_lazy("notes:secretkey_list")


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


def note_create_form_view(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            text_in = form.cleaned_data["text_in"]
            passkey_pk = form.cleaned_data["passkey"].pk
            save_note(text_in=text_in, passkey_pk=passkey_pk)
            needed_html = "notes/note_list.html"
        else:
            needed_html = "notes/note_form.html"

    else:
        form = NoteForm()
        needed_html = "notes/note_form.html"

    return render(
        request=request,
        template_name=needed_html,
        context=dict(
            notes_list=Note.objects.all(),
            form=form,
        ),
    )


def note_secret_form_view(request, pk):
    if request.method == "POST":
        form = NoteSecretForm(request.POST)

        if form.is_valid():
            #    text_in = form.cleaned_data["text_in"]
            #    passkey_pk = form.cleaned_data["passkey"].pk
            #    save_note(text_in=text_in, passkey_pk=passkey_pk)
            needed_html = "notes/note_list.html"
        else:
            needed_html = "notes/notesecret_form.html"

    else:
        form = NoteForm()
        needed_html = "notes/notesecret_form.html"

    return render(
        request=request,
        template_name=needed_html,
        context=dict(
            notes_list=Note.objects.all(),
            form=form,
        ),
    )


class NoteSecretView(FormView):
    model = Note
    form_class = NoteSecretForm
    template_name = "notes/notesecret_form.html"

    def get_success_url(self):
        return reverse_lazy("notes:notes_secretview", kwargs=dict(pk=self.kwargs["pk"]))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = Note.objects.get(pk=self.kwargs["pk"])
        passkey = kwargs["instance"].passkey
        text_out = kwargs["instance"].text_out
        kwargs["instance"].text_in = get_encrypt_decrypt_string(text_out, passkey.value, mode="decrypt", debug=False)
        return kwargs

    # def form_valid(self, form):
    #    form.save()
    #    return super().form_valid(form)
