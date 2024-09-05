from rest_framework import serializers
from .models import Order
from stock.models import Stock
from stock.serializers import StockSerializer
from cart.models import CartItem

class OrderSerializer(serializers.ModelSerializer):
    seller_name = serializers.CharField(source='seller_id.org_name', read_only=True)
    buyer_name = serializers.CharField(source='cart_id.buyer_id.org_name', read_only=True)
    class Meta:
        model = Order
        #fields = '__all__'
        fields = ['id', 'seller_id', 'seller_name', 'cart_id', 'buyer_name', 'total_cost', 'status']
        read_only_fields = ['total_cost']
    
    def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args, **kwargs)
        
        if self.context['request'].method != 'PUT':
            self.fields['status'].read_only = True
 
    def get_updated_stock(self, obj):
        stocks = Stock.objects.all()
        return StockSerializer(stocks, many=True).data
 
    def create(self, validated_data):
        order = super().create(validated_data)
        return order
 
    def update_stock(self, order):
        cart_items = CartItem.objects.filter(cart_id=order.cart_id)
        for item in cart_items:
            stock = Stock.objects.get(drug_id=item.drug_id)
            stock.quantity -= item.quantity
            stock.save()
        
        #delete the cart_item
        cart_items.delete()
        #delete the cart
        cart = order.cart_id
        cart.total_cost = 0
        cart.save(update_fields=['total_cost'])
 
    def update(self, instance, validated_data):
        previous_status = instance.status
        instance = super().update(instance, validated_data)
        if previous_status != 'approved' and instance.status == 'approved':
            self.update_stock(instance)
        return instance