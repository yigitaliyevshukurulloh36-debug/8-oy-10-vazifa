from django.urls import path, include
from .views import CompanyViewSet, WorkerViewSet, BuildingViewSet, CommentViewSet
from rest_framework.routers import SimpleRouter, DefaultRouter

router = SimpleRouter()
router.register('companies', CompanyViewSet)
router.register('workers', WorkerViewSet)
router.register('buildings', BuildingViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]