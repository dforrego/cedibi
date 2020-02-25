"""cedibi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from login import views as login_view
from bi import views as bi_view
from login.views import login, logout

urlpatterns = [
  path('admin/', admin.site.urls),
  url('api/', include('rest_framework.urls')),
  path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
  # get user
  path('api/v1/users/<int:pk>', login_view.UserList.as_view()),
  # get boards
  # create board
  path('api/v1/roles/<int:pk>/boards', bi_view.BoardListCreate.as_view()),
  # get board
  path('api/v1/boards/<int:pk>', bi_view.BoardObject.as_view()),
  # get graphs
  path('api/v1/boards/<int:pk>/graphs', bi_view.GraphList.as_view()),
  # get comments
  # create comments
  path('api/v1/boards/<int:pk>/comments', bi_view.CommentListCreate.as_view()),
  ###
  # login
  url('api/v1/login', login, name='login'),
  # login
  url('api/v1/logout', logout, name='logout'),
  
  path('docs/',
       include_docs_urls(title='Documentación API CeDiBI',
                         description="API para el análisis de datos",
                         public=True))
]
