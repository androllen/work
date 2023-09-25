# -*- coding: utf-8 -*-
import random
import time
from django.http import JsonResponse
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
#JsonResponse 默认传入参数是字典格式，如果不是，则报错。


#添加发布会接口
def add_event(request):
    #POST请求
    name = request.POST.get('name','')
    if name == '' :
        #ensure_ascii 禁用ascii码
        return JsonResponse({'status':10021,'message':'参数错误'},json_dumps_params={'ensure_ascii':False})

    return JsonResponse({'status':200,'message':'添加成功'})

# 发布会查询接口 http://127.0.0.1:8000/api/get_event_list/?name=33
def get_event_list(request):
    # GET请求
    name = request.GET.get('name','')
    if name == '':
        return JsonResponse({'status':10021,'message':'参数错误'})

    if name != '':
        return JsonResponse({'status':10022,'message':'3'})

#测试频道广播
def get(request):
    event = {}
    event["message"] = {"latitudenum":37.553534,"longitudenum":122.083534,"yaw":90}

    # channel_layer = get_channel_layer()     #重要代码
    # async_to_sync(channel_layer.group_send)("chat_live", {"type": "chat_message","message": event["message"]})   #重要代码

    # channel_layer = get_channel_layer()
    # event["message"] = payload = [random.randint(0, 100) for i in range(6)]
    # print(payload)
    # print(event["message"])
    # async_to_sync(channel_layer.group_send)('chat', {"type": "chat_message","message": event["message"]})

    t = threading.Thread(target=func)
    t.start()

    message = "ws send ok"
    return JsonResponse({"message": message})

def post(request):
    message = "post ok"

    return JsonResponse({"message": message})


import threading

def func():
    while True:
        event = {}
        channel_layer = get_channel_layer()
        event["message"] = payload = [random.randint(0, 100) for i in range(6)]
        print(payload)
        async_to_sync(channel_layer.group_send)('chat', {"type": "chat_message","message": event["message"]})        
        time.sleep(3)



