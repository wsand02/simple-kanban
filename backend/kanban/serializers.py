from rest_framework import serializers
from kanban.models import Board, List, Card

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ["id", "title", "owner"]
        read_only_fields = ["owner"]

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ["id", "title", "position"]
        read_only_fields = ["position"]

    def create(self, validated_data):
        # 'board' is passed via the view's context
        board = self.context.get('board')
        if board:
            validated_data['position'] = board.lists.count()
        return super().create(validated_data)

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["id", "title", "position"]
        read_only_fields = ["position"]

    def create(self, validated_data):
        list_obj = self.context.get('list')
        if list_obj:
            validated_data['position'] = list_obj.cards.count()
        return super().create(validated_data)