from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from bi.models import Board, Graph, Comment
from bi.serializers import BoardSerializer, GraphSerializer, CommentSerializer


class BoardListCreate(ListCreateAPIView):
    serializer_class = BoardSerializer
    
    def get_queryset(self):
        values = Board.objects.filter(rol=self.kwargs["pk"])
        return get_object_or_404(values)


class BoardObject(RetrieveAPIView):
    queryset = Board.objects.filter(pk=1)
    serializer_class = BoardSerializer
  
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class GraphList(ListAPIView):
    serializer_class = GraphSerializer
    
    def get_queryset(self):
        values = Graph.objects.filter(board=self.kwargs["pk"])
        return get_object_or_404(values)
      

class CommentListCreate(ListCreateAPIView):
    serializer_class = CommentSerializer
  
    def get_queryset(self):
        values = Comment.objects.filter(board=self.kwargs["pk"])
        return get_object_or_404(values)
