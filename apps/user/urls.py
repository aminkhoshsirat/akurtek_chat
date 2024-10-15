from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('sign-in', LoginView.as_view(), name='login'),
    path('sign-up', SignUpView.as_view(), name='sign_in'),
    path('logout', LogOutView.as_view(), name='logout'),
    path('status', StatusView.as_view(), name='status'),
    path('contacts', ContactsView.as_view(), name='contacts'),
    path('settings', SettingsView.as_view(), name='settings'),
    path('favorite', UserFavoriteView.as_view(), name='favorite'),
    path('document', UserDocumentView.as_view(), name='document'),
    path('to-do', UserToDoView.as_view(), name='to-do'),
    path('files', UserFilesView.as_view(), name='files'),
    path('note', UserNoteView.as_view(), name='note'),
    path('reminder', UserReminderList.as_view(), name='reminder'),
]
