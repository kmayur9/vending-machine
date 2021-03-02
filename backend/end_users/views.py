from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product,Denomination, Order, OrderItem
from end_users import serializers
# Create your views here.

""" All Product related APIs here"""
class ProductApiView(APIView):

	serializer_class = serializers.ProductSerializer

	""" return all available products"""
	def get(self, request, format=None):

		""" return all available products"""
		products = Product.objects.all()
		serializer = self.serializer_class(products, many=True)

		return Response({'status':'success', 'response':serializer.data})

	""" Create new products"""
	def post(self, request):

		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			prod_saved = serializer.save()

			return Response({"success": "Product '{}' created successfully".format(prod_saved.name)})

		else:
			return Response(
				serializer.errors,
				status=status.HTTP_400_BAD_REQUEST)

	""" Delete specified product"""
	def delete(self, request):

		products = Product.objects.all().delete()

		return Response({'status':'success', 'response':'Deleted Successfully'})


""" All denomination APIs here"""
class DenominationApiView(APIView):

	serializer_class = serializers.DenominationSerializer

	""" return all available denominatios"""
	def get(self, request, format=None):

		""" return all available products"""
		denominations = Denomination.objects.all()
		serializer = self.serializer_class(denominations, many=True)

		return Response({'status':'success', 'response':serializer.data})

	""" Create new Denomination"""
	def post(self, request):
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			denomination_saved = serializer.save()

			return Response({"success": "Denomination '{}' created successfully".format(denomination_saved.val)})

		else:
			return Response(
				serializer.errors,
				status=status.HTTP_400_BAD_REQUEST)

	""" Delete all Denominations"""
	def delete(self, request):

		denominations = Denomination.objects.all().delete()

		return Response({'status':'success', 'response':'Deleted Successfully'})


""" All Order APIs here"""
class OrderApiView(APIView):

	serializer_class = serializers.OrderSerializer

	""" get placed order details"""
	def get(self, request, format=None):

		# import pdb; pdb.set_trace()
		orders = Order.objects.all()
		serializer = self.serializer_class(orders, many=True)

		return Response({'status':'success', 'response':serializer.data})

	""" Place new order """
	def post(self, request):
		""" place order"""

		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			order_saved = serializer.save()

			return Response({"success": "Order '{}' created successfully".format(order_saved.Date)})

		else:
			return Response(
				serializer.errors,
				status=status.HTTP_400_BAD_REQUEST)

	""" Delete all Orders"""
	def delete(self, request):

		orders = Order.objects.all().delete()

		return Response({'status':'success', 'response':'Deleted Successfully'})
