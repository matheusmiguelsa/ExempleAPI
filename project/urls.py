from django.contrib import admin
from django.urls import include, path
from pages.views import ClientViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router =  routers.DefaultRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),
    # User Management
    path('accounts/', include('allauth.urls')),
    # Form
    path('', include('pages.urls', namespace='pages')),
    # API
    path('api/', include(router.urls)),
    # JWT
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
]