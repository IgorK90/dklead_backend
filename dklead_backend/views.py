from django.contrib.auth.models import User
from django.core.serializers import serialize, json
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpRequest
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import JSONParser

from dklead_backend.models import News, TeamMember, Project, Contact, About, Feedback
from dklead_backend.serializers import NewsSerializer, CreateNewsSerializer, TeamSerializer, CreateTeamSerializer, \
    ProjectSerializer, CreateProjectSerializer, ContactSerializer, AboutSerializer, FeedbackSerializer


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
        return JsonResponse({'message1':'news with id', 'id':id_, 'message2':'does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        news_ser = NewsSerializer(news,many=False)
        return JsonResponse(news_ser.data, safe=False)
    if request.method=='PUT':
        news_data = JSONParser().parse(request)
        news_serializer = CreateNewsSerializer(news, data = news_data)
        if news_serializer.is_valid():
            news_serializer.save()
            return JsonResponse(news_serializer.data, safe=False)
        return JsonResponse(news_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        news.delete()
        return(HttpResponse(f'news with id:{id_} deleted'))
    return HttpResponse(f"not working")


@api_view(['GET', 'POST'])
def list_team(request:HttpRequest)->JsonResponse:
    if request.method=='GET':
        team = TeamMember.objects.all()
        team_serializer = TeamSerializer(team, many=True)
        return JsonResponse(team_serializer.data, safe=False)
    elif request.method=='POST':
        # user = request.user
        # if not user.is_authenticated:
        #     return HttpResponseRedirect('/')
        team = JSONParser().parse(request)
        team_serializer = CreateTeamSerializer(data = team)
        print(team_serializer)
        if team_serializer.is_valid():
            team_serializer.save()
            return HttpResponse(f"good")
        else:
            return HttpResponse("bad")

@api_view (['GET', 'PUT', 'DELETE'])
def team_manipulate(request: HttpRequest, id_: int)->JsonResponse:
    try:
        team = TeamMember.objects.get(id=id_)
    except TeamMember.DoesNotExist:
        return JsonResponse({'message1':'TeamMember with id', 'id':id_, 'message2':'does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        team_ser = TeamSerializer(team, many=False)
        return JsonResponse(team_ser.data, safe=False)
    if request.method=='PUT':
        team_data = JSONParser().parse(request)
        team_ser = CreateTeamSerializer(team, data=team_data)
        if team_ser.is_valid():
            team_ser.save()
            return JsonResponse(team_ser.data, safe=False)
        else:
            return JsonResponse(team_ser.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        team.delete()
        return (HttpResponse(f'TeamMember with id:{id_} deleted'))
    return HttpResponse(f"not working")

@api_view(['GET', 'POST'])
def list_projects(request: HttpRequest)->JsonResponse:
    if request.method=='GET':
        projects =Project.objects.all()
        project_serializer = ProjectSerializer(projects, many=True)
        return JsonResponse(project_serializer.data, safe=False)
    if request.method=='POST':
        # user = request.user
        # if not user.is_authenticated:
        #     return HttpResponseRedirect('/')
        project =JSONParser().parse(request);
        project_serializer = CreateProjectSerializer(data=project)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse(project_serializer.data, safe=False)
        else:
            return JsonResponse({'message1':'bad request'})

@api_view(['GET', 'PUT', 'DELETE'])
def projects_manipulate(request: HttpRequest, id_:int)->JsonResponse:
    try:
        project = Project.objects.get(id=id_)
    except Project.DoesNotExist:
        return JsonResponse({'message1':'project with id', 'message2':id_, 'message3':'does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        project_serializer = ProjectSerializer(project, many=False)
        return JsonResponse(project_serializer.data, safe=False)
    if request.method=='PUT':
        projec_data =JSONParser().parse(request)
        project_serializer = CreateProjectSerializer(project,data = projec_data)
        if project_serializer.is_valid():
            project_serializer.save();
            return JsonResponse(project_serializer.data)
        else:
            return JsonResponse({'message1': 'wrong input data'}, status= status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    if request.method=='DELETE':
        project.delete()
        return JsonResponse({'message1':'project with id','message2':id_,'message3':'is deleted'},status=status.HTTP_200_OK)
    return HttpResponse(f'not working')

@api_view(['GET', 'POST'])
def list_contacts(request:HttpRequest)->JsonResponse:
    if request.method=='GET':
        contacts = Contact.objects.all()
        contacts_serializer  = ContactSerializer(contacts, many=True)
        return (JsonResponse(contacts_serializer.data, safe=False))
    if request.method=='POST':
        contact = JSONParser().parse(request);
        contact_serializer = ContactSerializer(data=contact)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return(JsonResponse(contact_serializer.data, safe=False))

@api_view(['GET','POST'])
def list_about_info(request:HttpRequest)->JsonResponse:
    if request.method=='GET':
        about_info = About.objects.all()
        about_serializer = AboutSerializer(about_info, many=True)
        return (JsonResponse(about_serializer.data, safe=False))
    if request.method=='POST':
        about_data = JSONParser().parse(request)
        about_serializer = AboutSerializer(data=about_data)
        if about_serializer.is_valid():
            about_serializer.save()
            return(JsonResponse(about_serializer.data, safe=False))

@api_view(['GET','POST'])
def list_feedback(request:HttpRequest)->JsonResponse:
    if request.method=='GET':
        feedback = Feedback.objects.all()
        feedback_serializer = FeedbackSerializer(feedback, many=True)
        return JsonResponse(feedback_serializer.data, safe=False)
    if request.method=='POST':
        feedback_data = JSONParser().parse(request)
        feedback_serializer = FeedbackSerializer(data=feedback_data)
        if feedback_serializer.is_valid():
            feedback_serializer.save()
            return JsonResponse(feedback_serializer.data, safe=False)

@api_view(['GET', 'DELETE'])
def feedback_manipulate(request:HttpRequest, id_:int)->JsonResponse:
    try:
        feedback = Feedback.objects.get(id=id_)
    except Feedback.DoesNotExist:
        return JsonResponse({'message1':'feedback with id', 'message2':id_, 'message3':'does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        feedback_serializer = FeedbackSerializer(feedback, many=False)
        return JsonResponse(feedback_serializer.data, safe=False)
    if request.method=='DELETE':
        feedback.delete()
        return JsonResponse({'message1':'deleted'})











