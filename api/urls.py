from api.views import instrutorViewSet, planosViewSet
# from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('instrutores', instrutorViewSet)
router.register('planos', planosViewSet)
urlpatterns = router.urls