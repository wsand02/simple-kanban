from django.shortcuts import get_object_or_404, render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from kanban.permissions import IsBoardOwner


# Create your views here.
from kanban.serializers import (BoardSerializer, ListSerializer, CardSerializer)

from kanban.models import Board

class BoardListCreateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        boards = Board.objects.filter(owner=request.user)
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoardDetailView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsBoardOwner]
    def get(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        self.check_object_permissions(request, board)
        serializer = BoardSerializer(board)
        return Response(serializer.data)

class ListListCreateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsBoardOwner]
    def get(self, request, board_pk):
        board = get_object_or_404(Board, pk=board_pk)
        self.check_object_permissions(request, board)
        lists = board.lists.all()
        serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)

    def post(self, request, board_pk):
        board = get_object_or_404(Board, pk=board_pk)
        self.check_object_permissions(request, board)
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(board=board)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
