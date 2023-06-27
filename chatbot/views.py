import os
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from core.models import PollsQuestion
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai

def ask_open_ai(input_messages):
    if input_messages:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = input_messages
        )
        return response.choices[0]
    return None


def replace_placeholders(text, replacements):
    for placeholder, value in replacements.items():
        text = text.replace(placeholder, value)
    return text


class ChatBot(View):
    def get(self, request, slug):
        questions = PollsQuestion.objects.filter(objecttype=slug)

        if slug == 'combinationdata':
            replacements = {
                "[CROP_NAME]": request.GET.get('parentcropid', 'Vegetables'),
                "[VARIETIES_NAME]": request.GET.get('mastercropid', 'Carrots'),
                "[HARVESTSTAGE_NAME]": request.GET.get('growingmethodid', 'Full-Size'),
            }

            for question in questions:
                question.questiontext = replace_placeholders(question.questiontext, replacements)

        return render(request, 'chatbot/chatbottemp.html', {"questions": questions})
                      
    def post(self, request, slug):
        message = request.POST['message']
        chatbot_response = ask_open_ai(message)
        return JsonResponse(chatbot_response)
    

class ChatBotView(APIView):
     def post(self, request):
        messages = request.data.get('messages')
        if messages:
            chatbot_response = ask_open_ai(messages)
            if chatbot_response:
                return Response(data=chatbot_response, status=status.HTTP_200_OK)
        return Response(data="No message found", status=status.HTTP_400_BAD_REQUEST)
