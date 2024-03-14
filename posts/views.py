from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication

from .serializers import PostSerializer
from .models import Posts
from .permissions import IsAuthorOrReadOnly


# Create your views here.

class PostListView(generics.ListAPIView):

    model = Posts
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):

    model = Posts
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthorOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)

    model = Posts
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
