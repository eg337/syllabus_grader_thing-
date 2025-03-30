from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from datetime import datetime

from .models import Grade_Calc
from .serializers import Grade_Calc_Serializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from grade_weight import generate_weights
import sys
import json
import subprocess


# def home(request):
#     return HttpResponse("Welcome to the backend!") 

def index(request):
    current_time = datetime.now().strftime("%-I:%S %p")
    current_date = datetime.now().strftime("%A %m %-Y")

    data = {
        'time': current_time,
        'date': current_date,
    }

    return JsonResponse(data)


class Create_Grade_Calc_View(APIView):
    serializer_class = Grade_Calc_Serializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            #input_data = request.data.get('input_data')
            input_file = request.FILES.get('input_file')
            for key in request.FILES:
                filename = request.FILES[key]._get_name()
                input_file = request.FILES[key].file
                print(request.FILES[key].content_type)

            weights = generate_weights(input_file, filename)
        

        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)