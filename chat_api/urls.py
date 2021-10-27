from django.urls import path
from . import views

urlpatterns = [
    path("messages/list/<int:page>/", views.MessagesListView.as_view(), name="messages_list"),
    path("messages/single/<int:pk>/", views.MessageSingleView.as_view(), name="messages_single"),
    path("messages/add/", views.MessageAddView.as_view(), name="messages_add"),
]
