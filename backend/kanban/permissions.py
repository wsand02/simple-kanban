from rest_framework.permissions import BasePermission

class IsBoardOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        if hasattr(obj, 'board'):
            return obj.board.owner == request.user
        if hasattr(obj, 'list'):
            return obj.list.board.owner == request.user
        if hasattr(obj, 'card'):
            return obj.card.list.board.owner == request.user
        return False