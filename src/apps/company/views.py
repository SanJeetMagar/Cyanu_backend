from rest_framework import generics
from .serializers import CompanyInfoSerializer, OutreachNumberSerializers, ContactSerializer
from rest_framework.permissions import AllowAny
from .models import CompanyInfo, OutreachNumber, ContactInfo

class CompanyInfoView(generics.ListAPIView):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer


class OutreachNumberView(generics.ListAPIView):
    queryset = OutreachNumber.objects.all()
    serializer_class = OutreachNumberSerializers


class ContactInfoView(generics.CreateAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactSerializer