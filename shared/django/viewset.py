from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet


class CreateUpdateDestroyListModelViewSet(CreateModelMixin,
                                          UpdateModelMixin,
                                          DestroyModelMixin,
                                          ListModelMixin,
                                          GenericViewSet):
    """
    A viewset that provides default `create()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass
