from django.shortcuts import render

from django.http.response import JsonResponse
from django.http.response import HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from webKomber.models import UserData
from webKomber.serializers import UserdataSerializer
from rest_framework.decorators import api_view
import json
from datetime import datetime
import pytz
# Create your views here.

LOCAL_TIMEZONE = pytz.timezone('Asia/Jakarta')

def index(request):
    userData = UserData.objects.all()
    hashLocData = dict()
    for i in userData:
        key = str(i.locations)
        hashLocData.setdefault(key,[])
        hashLocData[key].append(i)

    for key in hashLocData:
        bindStr = ""
        for i, item in enumerate(hashLocData[key]):
            localDate = item.created_at.replace(tzinfo=pytz.utc).astimezone(LOCAL_TIMEZONE)
            localDateStr = localDate.strftime('%d-%m-%Y %H:%M:%S') + " WIB"
            bindStr += "<b>" + str(i+1) + ". " + str(item.nama_user) + "</b><br>" + str(item.get_label_aktivitas_display()) + "<br>" + localDateStr + "<br><br>"
        hashLocData[key] = bindStr

    return render(request, 'index.html', {'user':hashLocData})

# @api_view(['GET'])
# def tampil_map(request):
    
#     # if request.method == 'GET':
#     #     #Tampil Map Logic
@api_view(['POST'])
def user_data_post(request):
    if request.method == 'POST':
        #Simpan User Data Logic

        jsonObj = json.loads(request.body.decode('utf-8'))
        print(jsonObj)
        jsonStr = '{"nama_user":' + '"' + jsonObj['nama_user'] + '"' + ',' + '"label_aktivitas":' + str(jsonObj['label_aktivitas']) + ',' + '"locations":' + str(jsonObj['locations']) + '}'
        print("Final " + str(json.loads(jsonStr)))
        jsonFinal = json.loads(jsonStr)
        # user_data = JSONParser().parse(jsonFinal)
        user_data_serializer = UserdataSerializer(data=jsonFinal)
        # print(user_data_serializer)
        print("Tes: ", user_data_serializer.is_valid())
        print("Error JSON: ", user_data_serializer.errors)
        if user_data_serializer.is_valid():
            user_data_serializer.save()
            return JsonResponse(user_data_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

all_entries = UserData.objects.all()
# print(all_entries)

@api_view(['GET'])
def user_data_get(request):
    if request.method == 'GET':
        userDatas = UserData.objects.all()
        
        nama_user = request.GET.get('nama_user', None)
        if nama_user is not None:
            userDatas = userDatas.filter(nama_user__icontains=nama_user)
        
        user_data_serializer = UserdataSerializer(userDatas, many=True)
        print(user_data_serializer)
        # for i in JsonResponse(user_data_serializer.data, safe=False).decode():
        #     print(i)
        return JsonResponse(user_data_serializer.data, safe='false')
        # 'safe=False' for objects serialization

def home(request):
    userData = user_data_get(request)
    # return userData
    # return render(request, "templates/tes.html", {'userData':userData})
