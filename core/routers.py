from rest_framework import routers

from core.user.viewsets import UserViewset
from core.auth.viewsets.register import RegisterViewset
from core.auth.viewsets.login import LoginViewSet
from core.auth.viewsets.refresh import RefreshViewSet

router = routers.SimpleRouter()

router.register(r'user', UserViewset, basename='user')
router.register(r'auth/register', RegisterViewset, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

urlpatterns = [
    *router.urls,
]