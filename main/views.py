from .serializers  import (CompanySerializer, WorkerSerializer, BuildingSerializer, CommentSerializer)
from .models import (Company, Worker, Building, Comment)
from .permision import MyAuthenticated, CommentAuthorPermission
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404

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
    permission_classes = [MyAuthenticated, CommentAuthorPermission]
    def get_queryset(self):
        return Comment.objects.filter(building_id=self.kwargs.get("building_id"))
    
    def perform_create(self, serializer):
        building = get_object_or_404(Building, pk=self.kwargs.get("building_id"))
        serializer.validated_data['user'] = self.request.user
        serializer.validated_data['building'] = building
        serializer.save()
        return serializer

