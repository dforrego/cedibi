from rest_framework import serializers
from bi.models import Board, Graph, Comment, Values, TypeBoard
from login.serializers import UserDataSerializer


class TypeBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeBoard
        fields = ['name', 'code']


class BoardSerializer(serializers.ModelSerializer):
    type = TypeBoardSerializer(many=False, read_only=True)
  
    class Meta:
        model = Board
        fields = ['name', 'description', 'type', 'status', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    user = UserDataSerializer(many=False, read_only=True)
  
    class Meta:
        model = Comment
        fields = ['message', 'user', 'created_at']


class PostCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['message', 'user', 'board']


class ValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Values
        fields = ['val_x', 'val_y', 'nam_x', 'nam_y', 'percent']

      
class GraphSerializer(serializers.ModelSerializer):
    values = ValuesSerializer(many=True, read_only=True)
    board = BoardSerializer(many=False, read_only=True)
    
    class Meta:
        model = Graph
        fields = ['name', 'values', 'board', 'state', 'created_at']
