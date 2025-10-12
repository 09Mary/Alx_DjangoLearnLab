from django.urls import path
from .views import NotificationListView, MarkNotificationReadView, MarkAllReadView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications-list'),
    path('<int:pk>/read/', MarkNotificationReadView.as_view(), name='notification-read'),
    path('mark-all-read/', MarkAllReadView.as_view(), name='notifications-mark-all-read'),
]
