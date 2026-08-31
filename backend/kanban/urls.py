from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from kanban import views

urlpatterns = [
    path("boards/", views.BoardListCreateView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)