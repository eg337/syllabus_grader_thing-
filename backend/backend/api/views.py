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
from .grade_weight import generate_weights
from .deadline_gen import parse_schedule
from .write_xlsx import write_calc
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

# class Upload_View(APIView):
#     serializer_class = Grade_Calc_Serializer
    


class Create_Grade_Calc_View(APIView):
    serializer_class = Grade_Calc_Serializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        # print("Init serial")
        serializer = self.serializer_class(data = request.data)
        # print("End init serial")
        deadline = {}
        if serializer.is_valid():
            #input_data = request.data.get('input_data')
            input_file = request.FILES.get('input_file')
            count = 0
            for key in request.FILES:
                # print("CHECKALLCAPS" + str(count) + "\n")
                # print(str(key) + "\n")
                filename = request.FILES[key]._get_name()
                # print(filename)
                input_file = request.FILES[key].file
                # print(request.FILES[key].content_type)
                if count == 0:
                    weights = generate_weights(input_file
                                       , filename)
                elif count == 1:
                    deadline = parse_schedule(weights["grade weights"], input_file, filename)
                count += 1
            # weights = generate_weights(input_file
            #                            , filename)
            if len(deadline) <1:
                deadline = parse_schedule(weights["grade weights"], input_file, filename)
            return write_calc(weights["grade weights"], deadline, weights["course title"])

            # xlsx = write_calc(weights, deadline)

            # response = HttpResponse(content_type='application/vnd.ms-excel')
            # response['Content-Disposition'] = 'attachment; filename=your_template_name.xlsx'
            # response.write(xlsx)
            # return response
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)