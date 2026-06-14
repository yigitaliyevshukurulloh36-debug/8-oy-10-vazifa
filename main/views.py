from .serializers  import (CompanySerializer, WorkerSerializer, BuildingSerializer, CommentSerializer)
from .models import (Company, Worker, Building, Comment)
from rest_framework.viewsets import ModelViewSet

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class WorkerViewSet(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class BuildingViewSet(ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

