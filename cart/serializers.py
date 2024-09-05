from rest_framework import serializers
from .models import Cart, CartItem

class CartSerializer(serializers.ModelSerializer):
    org_name = serializers.CharField(source='buyer_id.org_name', read_only=True)
    class Meta:
        model = Cart
        fields = ['id', 'buyer_id', 'org_name', 'total_cost']
        read_only_fields = ['total_cost']

class CartItemSerializer(serializers.ModelSerializer):
    org_name = serializers.CharField(source='cart_id.buyer_id.org_name', read_only=True)
    drug_name = serializers.CharField(source='drug_id.name', read_only=True)
    class Meta:
        model = CartItem
        fields = ['id', 'cart_id', 'org_name', 'drug_id', 'drug_name', 'quantity', 'item_cost']
        read_only_fields = ['item_cost']
        
    def validate(self, data):
        drug = data['drug_id']
        quantity = data['quantity']
        data['item_cost'] = drug.price * quantity
        return data
