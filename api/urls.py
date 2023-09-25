from django.urls import path
from api.views import add_event,get_event_list,get

#在api下创建urls.py，配置具体接口的二级目录

urlpatterns = [
    # guest system interface:
    path('get/',get,name='get'),
    # ex : /api/add_event/
    path('add_event/',add_event,name='add_event'),
    # ex : /api/get_event_list/
    path('get_event_list/',get_event_list,name='get_event_list'),
]