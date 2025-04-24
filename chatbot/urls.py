# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.chatbot_view, name='chatbot'),
#     path('chat-api/', views.chat_api, name='chat_api'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_view, name='chatbot'),
    path('chat-api/', views.chat_api, name='chat_api'),
]
