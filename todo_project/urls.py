from django.contrib import admin
from django.urls import path, include
# from rest_framework.authtoken import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    #path('api/token-auth/', views.obtain_auth_token, name='api_token_auth'),

    # Для отримання пари токенів (access, refresh)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Для оновлення access-токе
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Повертає сам файл schema.yml (машиночитний опис)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # UI (Swagger)
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'
    ),

    # Альтернативний UI (ReDoc)
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'
    ),
]
