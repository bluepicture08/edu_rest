from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

#장고 레스트 프레임워크는 라우터를 통해 url을 결정합니다.

router = DefaultRouter() #라우트 정의.
router.register('post', views.PostViewSet) #라우드 등록

urlpatterns = [
    path('', include(router.urls)), #CRUD에 해당하는 URL을 설정해 주는 것.
]
