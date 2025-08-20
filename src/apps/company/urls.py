from django.urls import path
from .views import CompanyInfoView, OutreachNumberView

urlpatterns = [
    path("info/", CompanyInfoView.as_view(), name = "company_info" ),
    path("outreachnumber/", OutreachNumberView.as_view(), name="outreachnumber"),
]