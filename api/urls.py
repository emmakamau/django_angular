from django.urls import path
from . import views

urlpatterns = [
    path('department/', views.departmentApi),
    path('department/<int:id>/', views.departmentApi),

    path('employee/', views.employeeApi),
    path('employee/<int:id>/', views.employeeApi)
]