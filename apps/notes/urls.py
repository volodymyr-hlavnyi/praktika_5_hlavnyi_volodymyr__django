from django.urls import path

from . import views

app_name = "notes"

urlpatterns = [
    path("list/", views.NotesListView.as_view(), name="notes_list"),
    path("listkey/", views.SecretKeyListView.as_view(), name="secretkey_list"),
    #
    #    path("delete/", views.delete_contacts_view, name="contacts_delete"),
    path("delete/<int:pk>/", views.NoteDeleteView.as_view(), name="notes_delete"),
    path("deletekey/<int:pk>/", views.SecretKeyDeleteView.as_view(), name="secretkey_delete"),
    #
    path("edit/<int:pk>/", views.NoteEditView.as_view(), name="note_edit"),
    path("editkey/<int:pk>/", views.SecretKeyEditView.as_view(), name="secretkey_edit"),
    #
    #    path("generate/", views.generate_contacts_view, name="contacts_generate"),
    #
    path("create/", views.NoteCreateView.as_view(), name="notes_create"),
    #
    path("createkey/", views.SecretKeyCreateView.as_view(), name="secretkey_create"),
    #    path("detail/<int:pk>/", views.ContactDetailView.as_view(), name="contacts_detail"),
]
