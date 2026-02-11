from django.urls import path
from .api_views import (
    TaskListCreateAPI,
    TaskRetrieveUpdateDeleteAPI
)

urlpatterns = [
    path('tasks/', TaskListCreateAPI.as_view()),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDeleteAPI.as_view()),
]
