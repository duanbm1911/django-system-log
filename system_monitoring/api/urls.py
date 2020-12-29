from django.urls import path
from . import views

urlpatterns = [
    path('log/', views.api_log_request),
    # path('log/<int:pk>', views.api_log_detail)
]
