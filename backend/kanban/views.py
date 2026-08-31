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

from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from kanban.models import Board, List, Card
from kanban.serializers import BoardSerializer, ListSerializer, CardSerializer
from kanban.permissions import IsBoardOwner


# ---------- BOARD ENDPOINTS ----------

class BoardListCreateView(generics.ListCreateAPIView):
    """List all boards for the current user, or create a new board."""
    serializer_class = BoardSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BoardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a specific board."""
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsBoardOwner]
    lookup_field = 'pk'  # matches URL <int:pk>


# ---------- LIST ENDPOINTS (Nested under Board) ----------

class ListListCreateView(generics.ListCreateAPIView):
    """List all lists of a board, or create a new list within that board."""
    serializer_class = ListSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsBoardOwner]

    def get_queryset(self):
        board_pk = self.kwargs.get('board_pk')
        board = get_object_or_404(Board, pk=board_pk)
        self.check_object_permissions(self.request, board)
        return board.lists.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        board_pk = self.kwargs.get('board_pk')
        context['board'] = get_object_or_404(Board, pk=board_pk)
        return context

    def perform_create(self, serializer):
        board_pk = self.kwargs.get('board_pk')
        board = get_object_or_404(Board, pk=board_pk)
        self.check_object_permissions(self.request, board)
        serializer.save(board=board)


class ListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a specific list."""
    queryset = List.objects.all()
    serializer_class = ListSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsBoardOwner]
    lookup_field = 'pk'

    # No need to manually check permissions – DRF passes the List object
    # to IsBoardOwner, which knows how to navigate to board.owner.


# ---------- CARD ENDPOINTS (Nested under List) ----------

class CardListCreateView(generics.ListCreateAPIView):
    """List all cards of a list, or create a new card within that list."""
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


class CardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a specific card."""
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsBoardOwner]
    lookup_field = 'pk'