from django.shortcuts import render
from .models import Post
from .serializer import PostSerializer
from rest_framework import viewsets

#cbv 기반이기 때문
class PostViewSet(viewsets.ModelViewSet): #API상의  CRUD를 담당해주는 것
    queryset = Post.objects.all()
    serializer_class = PostSerializer
