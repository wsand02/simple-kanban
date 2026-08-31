from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from kanban import views

urlpatterns = [
    path("boards/", views.BoardListCreateView.as_view()),
    path("boards/<int:pk>", views.BoardDetailView.as_view()),
    path("boards/<int:board_pk>/lists/", views.ListListCreateView.as_view()),
    path("boards/<int:board_pk>/lists/<int:list_pk>/cards/", views.CardListCreateView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)