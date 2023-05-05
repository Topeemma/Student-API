
from django.contrib import admin
from django.urls import path, include
from student import views

from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Student Api",
        default_version="v1.0.0",
        description="An API for student ",
        contact=openapi.Contact(email="tope.manny@gmail.com"),
        license=openapi.License(name="MIT License"),
    ), 
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/', include('student.urls')),

    path('swag/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc'), name='schema-redoc'),
]
