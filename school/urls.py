# from django.contrib import admin
# from django.urls import path,include
# from . import views

# urlpatterns = [
#    path('',views.index, name="index"),
#    path('dashboard/', views.dashboard, name='dashboard'), 
#    path('notification/mark-as-read/', views.mark_notification_as_read, name='mark_notification_as_read' ),
#    path('notification/clear-all', views.clear_all_notification, name= "clear_all_notification")
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Notifications
    path('notification/mark-as-read/', views.mark_notification_as_read, name='mark_all_notifications_as_read'),
    path('notification/mark-as-read/<uuid:notification_id>/', views.mark_notification_as_read, name='mark_single_notification_as_read'),
    path('notification/clear-all/', views.clear_all_notification, name="clear_all_notification"),
]
