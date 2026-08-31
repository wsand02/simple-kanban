from django.shortcuts import get_object_or_404, render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from kanban.permissions import IsBoardOwner


# Create your views here.
from kanban.serializers import (BoardSerializer, ListSerializer, CardSerializer)

from kanban.models import Board, List

class BoardListCreateView(generics.ListCreateAPIView):
    serializer_class = BoardSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BoardDetailView(generics.RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsBoardOwner]
    lookup_field = 'pk'  # matches your URL pattern


# --- List Views (Nested under Board) ---

class ListListCreateView(generics.ListCreateAPIView):
    serializer_class = ListSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsBoardOwner]

    def get_queryset(self):
        board_pk = self.kwargs.get('board_pk')
        board = get_object_or_404(Board, pk=board_pk)
        self.check_object_permissions(self.request, board)
        return board.lists.all()

    def get_serializer_context(self):
        # Add the board to the serializer context for position calculation
        context = super().get_serializer_context()
        board_pk = self.kwargs.get('board_pk')
        context['board'] = get_object_or_404(Board, pk=board_pk)
        return context

    def perform_create(self, serializer):
        board_pk = self.kwargs.get('board_pk')
        board = get_object_or_404(Board, pk=board_pk)
        self.check_object_permissions(self.request, board)
        # Save with only the foreign key – context is already set
        serializer.save(board=board)


class CardListCreateView(generics.ListCreateAPIView):
    serializer_class = CardSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsBoardOwner]

    def get_queryset(self):
        list_pk = self.kwargs.get('list_pk')
        list_obj = get_object_or_404(List, pk=list_pk)
        self.check_object_permissions(self.request, list_obj.board)
        return list_obj.cards.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        list_pk = self.kwargs.get('list_pk')
        context['list'] = get_object_or_404(List, pk=list_pk)
        return context

    def perform_create(self, serializer):
        list_pk = self.kwargs.get('list_pk')
        list_obj = get_object_or_404(List, pk=list_pk)
        self.check_object_permissions(self.request, list_obj.board)
        serializer.save(list=list_obj)