from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from webKomber.models import UserData
from webKomber.serializers import UserdataSerializer
from rest_framework.decorators import api_view
import json
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

# @api_view(['GET'])
# def tampil_map(request):
    
#     # if request.method == 'GET':
#     #     #Tampil Map Logic
@api_view(['POST'])
def user_data_post(request):
    
    if request.method == 'POST':
        #Simpan User Data Logic
        user_data = JSONParser().parse(request)
        print(user_data)
        # user_data = json.loads(str(request.body.decode('utf-8')))
        user_data_serializer = UserdataSerializer(data=user_data)
        print(user_data_serializer)
        print("Tes: ", user_data_serializer.is_valid())
        if user_data_serializer.is_valid():
            user_data_serializer.save()
            return JsonResponse(user_data_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

all_entries = UserData.objects.all()
print(all_entries)

@api_view(['GET'])
def user_data_get(request):
    if request.method == 'GET':
        userDatas = UserData.objects.all()
        
        nama_user = request.GET.get('nama_user', None)
        if nama_user is not None:
            userDatas = userDatas.filter(nama_user__icontains=nama_user)
        
        user_data_serializer = UserdataSerializer(userDatas, many=True)
        return JsonResponse(user_data_serializer.data, safe=False)
        # 'safe=False' for objects serialization