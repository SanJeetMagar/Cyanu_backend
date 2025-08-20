from django.urls import path
from .views import CompanyInfoView, OutreachNumberView, ContactInfoView

urlpatterns = [
    path("info/", CompanyInfoView.as_view(), name = "company_info" ),
    path("outreachnumber/", OutreachNumberView.as_view(), name="outreachnumber"),
    path("contacts/", ContactInfoView.as_view(), name=  "contacts"),
]