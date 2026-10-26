from rest_framework import serializers
from .models import Client,Compte,Transaction,Agent,DemandeCredit,Remboursement

class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class CompteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Compte
        fields = '__all__'

class TransactionSerialiers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class AgentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class DemandeCreditSerializers(serializers.ModelSerializer):
    class Meta:
        model = DemandeCredit
        fields = '__all__'

class RemboursementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Remboursement
        fields = '__all__'