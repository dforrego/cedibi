from django.shortcuts import get_object_or_404
from oauth2_provider.contrib.rest_framework import IsAuthenticatedOrTokenHasScope
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from bi.models import Board, Graph, Comment
from bi.serializers import BoardSerializer, GraphSerializer, CommentSerializer


class BoardListCreate(ListCreateAPIView):
    serializer_class = BoardSerializer
    permission_classes = (IsAuthenticatedOrTokenHasScope,)
    required_scopes = ['read']
    
    def get_queryset(self):
        values = Board.objects.filter(rol=self.kwargs["pk"])
        return get_object_or_404(values)


class BoardObject(RetrieveAPIView):
    serializer_class = BoardSerializer
    permission_classes = (IsAuthenticatedOrTokenHasScope,)
    required_scopes = ['read']
    
    def get_queryset(self):
        values = Board.objects.filter(pk=self.kwargs["pk"])
        return get_object_or_404(values)
  
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class GraphList(ListAPIView):
    serializer_class = GraphSerializer
    permission_classes = (IsAuthenticatedOrTokenHasScope,)
    required_scopes = ['read']
    
    def get_queryset(self):
        values = Graph.objects.filter(board=self.kwargs["pk"])
        return get_object_or_404(values)
      

class CommentListCreate(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrTokenHasScope,)
    required_scopes = ['read']
  
    def get_queryset(self):
        values = Comment.objects.filter(board=self.kwargs["pk"])
        return get_object_or_404(values)
