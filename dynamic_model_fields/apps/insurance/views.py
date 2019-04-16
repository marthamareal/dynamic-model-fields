from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import RiskType, FieldType

from .serializers import RiskTypeSerializer, FieldTypeSerializer

from .renderers import ApiRenderer


class Paginator(PageNumberPagination):
    page_size = 6


class RiskTypeView(generics.ListCreateAPIView):
    """View for creating and listing risk types """

    serializer_class = RiskTypeSerializer
    queryset = RiskType.objects.prefetch_related('fields')
    renderer_classes = ApiRenderer,
    pagination_class= Paginator

class SingleRiskTypeView(generics.RetrieveUpdateDestroyAPIView):
    """View for updateing, deleting, and retrieving a single risk type """

    serializer_class = RiskTypeSerializer
    queryset = RiskType.objects.all()
    renderer_classes = ApiRenderer,

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message":"Risk Type Deleted successfully"}, status=status.HTTP_200_OK)

class FeildTypeView(generics.ListAPIView):
    """View for listing field types """
    
    serializer_class = FieldTypeSerializer
    queryset = FieldType.objects.all()
    renderer_classes = ApiRenderer,
