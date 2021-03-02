from rest_framework import serializers

from .models import Product, OrderItem, Denomination, Order

""" Product Serializer"""
class ProductSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=255)
	url = serializers.CharField(max_length=255)
	price = serializers.IntegerField()

	def create(self, validated_data):
		return Product.objects.create(**validated_data)

""" Denominations Serializer"""
class DenominationSerializer(serializers.Serializer):
	currency = serializers.CharField(max_length=255)
	val = serializers.IntegerField()

	def create(self, validated_data):
		return Denomination.objects.create(**validated_data)

""" OrderItems Serializer"""
class OrderItemsSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    orders = OrderItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('Date','Order_Value','orders')
