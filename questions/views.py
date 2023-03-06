from django.shortcuts import render
import requests
import openai

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from .models import Questions
from .serializers import QuestionsSerializer, QuestionTitleSerializer, QuestionDetailsSerializer, TextSerializer
from keys import API_KEY


class CustomPagination(PageNumberPagination):
    page_size = 5


    

class QuestionsView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    pagination_class = CustomPagination
    


class TitleListView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionTitleSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 5

class QuestionsDetailView(RetrieveAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionDetailsSerializer
    lookup_field = 'no'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    


class CleanTextAPIView(generics.GenericAPIView):
    serializer_class = TextSerializer  # define your serializer

    def post(self, request, *args, **kwargs):
        text = request.data.get('text')
        cleaned_text = self.clean_text(text)
        return Response({'cleaned_text': cleaned_text})

    def clean_text(self, text):
        # send text to ChatGPT API for processing

        #openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = API_KEY

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Write the answer to this question but only print out the first 100 words of the academic answer {text}",
            temperature=0,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0
        )

        cleaned_text = response['choices'][0]['text']

        return cleaned_text
