# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json

def fbLogin(request):
    return render(request, 'login.html')

@api_view(['POST', 'GET'])
def apifblogin(request):
    details = json.loads(requests.get("https://graph.facebook.com/me?access_token="+request.DATA['accesstoken']).content)
    if "error" not in details:
        name = details['name']
        mailid = details['email']
        return Response({'name':name}, 200)
    return Response({'error':"Not a valid user"}, 400)