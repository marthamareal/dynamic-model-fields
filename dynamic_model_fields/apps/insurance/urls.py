
from django.urls import path, include
from . import views

urlpatterns = [
    path('risk-types/', views.RiskTypeView.as_view(), name='list_create_views'),
    path('risk-types/<pk>/', views.SingleRiskTypeView.as_view(), name='update_retrieve_destroy'),
    path('field-types/', views.FeildTypeView.as_view(), name='field-types-list_view'),
]