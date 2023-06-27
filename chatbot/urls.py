from django.urls import path

from . import views

app_name = 'chatbot'
urlpatterns = [
    path('<slug:slug>', views.ChatBot.as_view(), name='chatbot'),
    path('api/conversation', views.ChatBotView.as_view(), name='chatbotconversation'),
]