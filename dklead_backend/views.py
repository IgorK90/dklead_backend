from django.contrib.auth.models import User
from django.core.serializers import serialize, json
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpRequest
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import JSONParser

from dklead_backend.models import News
from dklead_backend.serializers import NewsSerializer, CreateNewsSerializer


@api_view(['GET', 'POST'])
def list_news(request:HttpRequest)->JsonResponse:
    if request.method =='GET':
        news = News.objects.all()
        news_serializer = NewsSerializer(news, many=True)
        return JsonResponse(news_serializer.data, safe=False)
    elif request.method=='POST':
        # user = request.user
        # if not user.is_authenticated:
        #     return HttpResponseRedirect("/login")
        news_data = JSONParser().parse(request)
        news_serializer = CreateNewsSerializer(data = news_data)
        if news_serializer.is_valid():
            news_serializer.save()
            return HttpResponse(f'good')
        else:
            return HttpResponse(f'bad {news_serializer}')
    else:
        return HttpResponseRedirect('/')


def create_user(request)->HttpResponse:
    users = User.objects.all();
    user = User.objects.create_user("user", "user@user.com", "user")
    return HttpResponse(f"{user.name} is created")

@api_view(['GET', 'PUT', 'DELETE'])
def news_manipulate( request: HttpRequest, id_:int)->JsonResponse:
    try:
        news = News.objects.get(id=id_)
    except News.DoesNotExist:
        return JsonResponse({'message':'news with id {id_} does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        news_ser = NewsSerializer(news,many=False)
        return JsonResponse(news_ser.data, safe=False)
    if request.method=='PUT':
        news_data = JSONParser().parse(request)
        news_serializer = CreateNewsSerializer(news, data = news_data)
        if news_serializer.is_valid():
            news_serializer.save()
            print("saved msg")
            print(news_serializer.data)
            # dat = serialize('json', news_serializer)
            return JsonResponse(news_serializer.data, safe=False)
        return JsonResponse(news_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse(f"not working")