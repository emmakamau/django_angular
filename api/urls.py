from django.urls import path
from . import views

urlpatterns = [
    path('department/', views.departmentApi),
    path('department/<int:id>/', views.departmentApi)
]