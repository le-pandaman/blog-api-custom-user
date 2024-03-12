from django.shortcuts import render
from rest_framework import generics


from .serializers import PostSerializer
from .models import Posts


# Create your views here.

class PostListView(generics.ListAPIView):

    model = Posts
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):

    model = Posts
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    model = Posts
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
