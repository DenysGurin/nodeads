from groups.models import Group, Element
from groups.serializers import GroupListSerializer, ElementSerializer

from rest_framework import generics, pagination
from rest_framework.permissions import IsAdminUser


class CustomPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_guery_param = 'page_size'
    max_page_size = 10


class GroupList(generics.ListAPIView):
    """
    get:
    Return a list of all the existing groups.
    """
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer
    pagination_class = CustomPagination


class GroupDetail(generics.RetrieveAPIView):
    """
    get:
    Return the given group.
    """
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer
    

class ElementList(generics.CreateAPIView):
    """
    post:
    Create a new element instance.
    """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer


class ElementDetail(generics.RetrieveAPIView):
    """
    get:
    Return the given element.
    """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
