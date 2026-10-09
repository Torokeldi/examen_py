from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import TaskViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="task")

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('', include(router.urls)),
]

