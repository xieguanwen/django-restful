from django.shortcuts import render_to_response
from django.http import JsonResponse
from poststation.serializers import PoststationSerializer
from poststation.models import ShoujiPoststation
import json

def list(request):
    serializer = PoststationSerializer(ShoujiPoststation.objects.all(), many=True)
    return JsonResponse({'data':serializer.data,'error':0,'message':'success'})