from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProjectList.as_view(), name='projects'),
    path('<int:project_id>/', views.ProjectDetail.as_view(), name='project_detail'),
]
