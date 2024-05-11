from django.urls import path
from category.views import DashboardView

app_name = "category"

urlpatterns = [

    path("dashboard/",    DashboardView.as_view(),    name="dashboard"),
    
]