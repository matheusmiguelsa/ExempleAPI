from rest_framework import serializers
from pages.models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id', 'payment_id', 'start_date', 'end_date', 'original_value', 
            'collaborator_owner', 'social_bussiness_name', 'CNPJ'
        ]