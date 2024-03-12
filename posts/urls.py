from django.urls import path

from .views import PostListView, PostRetrieveUpdateDestroyAPIView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list_api'),
    path('new/', PostCreateView.as_view(), name='post_create_api'),
    path('<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post_api'),
]
