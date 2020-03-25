from django.urls import path, include
from rest_framework.routers import DefaultRouter

from anyclass import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'acts', views.ActViewSet)
router.register(r'time_table', views.TimeTableViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
   path('', include(router.urls)),
]
