from django.contrib import admin
from kanban.models import Board, Card, List

# Register your models here.
admin.site.register(Board)
admin.site.register(Card)
admin.site.register(List)