from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response


class ReviewTargetViewset(viewsets.ModelViewSet):
    serializer_class = ReviewTargetSerializer
    queryset = ReviewTarget.objects.all()
    http_method_names = ['get']


class GroupViewset(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = ReviewTarget.objects.all()
    http_method_names = ['get']


class ReviewViewset(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class ChartDataViewset(viewsets.ViewSet):
    def list(self, request):
        r = Review.objects.filter(
            target=request.query_params.get('target')
        )
        serialized = ChartDataSerializer(r, many=True)
        return Response(serialized.data, status=200)
