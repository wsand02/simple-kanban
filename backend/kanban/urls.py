from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from kanban import views

urlpatterns = [
    path('boards/', views.BoardListCreateView.as_view(), name='board-list-create'),
    path('boards/<int:pk>/', views.BoardRetrieveUpdateDestroyView.as_view(), name='board-detail'),

    # Lists (nested under a board)
    path('boards/<int:board_pk>/lists/', views.ListListCreateView.as_view(), name='list-list-create'),
    path('boards/<int:board_pk>/lists/<int:pk>/', views.ListRetrieveUpdateDestroyView.as_view(), name='list-detail'),

    # Cards (nested under a list)
    path('boards/<int:board_pk>/lists/<int:list_pk>/cards/', views.CardListCreateView.as_view(), name='card-list-create'),
    path('boards/<int:board_pk>/lists/<int:list_pk>/cards/<int:pk>/', views.CardRetrieveUpdateDestroyView.as_view(), name='card-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)