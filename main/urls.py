from django.urls import path, include
from .views import CompanyViewSet, WorkerViewSet, BuildingViewSet, CommentViewSet
from rest_framework.routers import SimpleRouter, DefaultRouter

router = SimpleRouter()
router.register('companies', CompanyViewSet)
router.register('workers', WorkerViewSet)
router.register('buildings', BuildingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('buildings/<int:building_id>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('buildings/<int:building_id>/comments/<int:comment_id>/', CommentViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}
    ), name='comment-detail')
]