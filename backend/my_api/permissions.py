from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    許可されたオーナーのみ対象のオブジェクトの編集ができるカスタム権限
    """

    def has_object_permission(self, request, view, obj):
        # 任意のリクエストについて、読み込んだ権限を許可する
        # GET、HEAD、OPTIONSリクエストをいつも許可する
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
