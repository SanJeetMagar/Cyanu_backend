from rest_framework import generics
from .serializers import CompanyInfoSerializer, OutreachNumberSerializers
from rest_framework.permissions import AllowAny
from .models import CompanyInfo, OutreachNumber

class CompanyInfoView(generics.ListAPIView):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer


class OutreachNumberView(generics.ListAPIView):
    queryset = OutreachNumber.objects.all()
    serializer_class = OutreachNumberSerializers

