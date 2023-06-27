from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from core.serializers import CombinationdataSerializer, PollsQuestionSerializer
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView

# Index loader page
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class IndexClass(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the polls index.")
    
    def post(self, request):
        return render(request, 'index.html', {})


class CombinationdataViewSet(APIView):
    def post(self, request):
        serializer = CombinationdataSerializer(data=request.data)
        if serializer.is_valid():
            # my_object = serializer.save()
            # Do something with the object
            return Response("Success")
        else:
            return Response(serializer.errors, status=400)
        
        # queryset = Combinationdata.objects.all()
        # serializer_class = CombinationdataSerializer(queryset, many=True)
        # return Response(data=serializer_class.data, status=status.HTTP_200_OK)


class PollsQuestionViewSet(APIView):
     def post(self, request):
        serializer = PollsQuestionSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            my_object = serializer.save()
            return Response("Success")
        else:
            return Response(serializer.errors, status=400)
    
