from rest_framework import serializers
from .models import Stock
from django.core.exceptions import ValidationError

class StockSerializer(serializers.ModelSerializer):
    drug_name = serializers.CharField(source='drug_id.name', read_only=True)
    class Meta:
        model = Stock
        fields = ['id', 'drug_id', 'drug_name', 'quantity']

    def update(self, instance, validated_data):
        drug = validated_data.get('drug_id')
        quantity = validated_data.get('quantity')

        existing_stock = Stock.objects.filter(drug_id=drug).first()

        quantity = validated_data.get('quantity', instance.quantity)
        if quantity < 0 and existing_stock.quantity < -1 * quantity:
            raise ValidationError("There is not enough quantity left")
        instance.quantity = existing_stock.quantity + quantity
        instance.save(update_fields=['quantity'])
        return instance