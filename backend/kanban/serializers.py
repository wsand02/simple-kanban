from rest_framework import serializers
from kanban.models import Board, List, Card

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ["id", "title", "owner"]

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ["title", "board", "position"]

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["title", "list", "position"]