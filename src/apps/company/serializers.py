from rest_framework import serializers
from .models import CompanyInfo, OutreachNumber

class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = "__all__"


class OutreachNumberSerializers(serializers.ModelSerializer):
    class Meta:
        model = OutreachNumber
        fields = "__all__"