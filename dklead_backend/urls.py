"""
URL configuration for dklead_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from dklead_backend.views import list_news, create_user, news_manipulate, list_team, team_manipulate, list_projects, \
    projects_manipulate, list_contacts, list_about_info, list_feedback, feedback_manipulate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/news', list_news),
    path('api/news/<int:id_>', news_manipulate),
    path('api/team', list_team),
    path('api/team/<int:id_>', team_manipulate),
    path('api/projects', list_projects),
    path('api/projects/<int:id_>', projects_manipulate),
    path('api/contacts', list_contacts),
    path('api/about', list_about_info),
    path('api/feedback', list_feedback),
    path('api/feedback/<int:id_>', feedback_manipulate),
    path('create_user/', create_user),
]
