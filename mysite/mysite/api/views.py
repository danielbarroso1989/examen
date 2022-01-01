import json
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.authentication import BasicAuthentication
from mysite.api.utils import search_symbol,validatedata
from django.shortcuts import  redirect
from django.contrib import messages
class GetTest(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):

        validate_symbol = search_symbol("MMM")

        return JsonResponse({"hola":"ok"}, status=status.HTTP_200_OK)

class CreateCompany(APIView):
   
    
    def post(self, request):

    
        validated  = validatedata(request.POST)

        if validated=="OK":
            
            return redirect("list_form")
        
        messages.error(request, validated)

        return redirect("createform")

    
