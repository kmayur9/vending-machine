from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Product,Denomination, Order, OrderItem



class ModelTests(TestCase):

    def setUp(self):
        Product.objects.create(name="coke", price=99)
        Denomination.objects.create(currency="dollar", val=99)
        Order.objects.create(Order_Value=199)
        OrderItem.objects.create(Order = Order.objects.get(), Product = Product.objects.get(name="coke"), Quantity=99)


    def test_create_product(self):
        """Test creating product """
        coke = Product.objects.get(name="coke")
        self.assertEqual(coke.price,99)

    def test_create_denomination(self):
        """Test creating Denomination """
        dollar = Denomination.objects.get(currency="dollar")
        self.assertEqual(dollar.val,99)

    def test_delete_denomination(self):
        """Test deleting Denomination """
        # import pdb; pdb.set_trace()
        Denomination.objects.all().delete()
        denominations_count = Denomination.objects.count()

        self.assertEqual(denominations_count,0)


    def test_create_order(self):
        """Test creating Order """
        order = Order.objects.get()
        self.assertEqual(order.Order_Value,199)

    def test_delete_order(self):
        """Test deleting Order """
        # import pdb; pdb.set_trace()
        Order.objects.all().delete()
        order_count = Order.objects.count()

        self.assertEqual(order_count,0)


    def test_delete_product(self):
        """Test deleting product """
        # import pdb; pdb.set_trace()


        Product.objects.all().delete()
        products_count = Product.objects.count()

        self.assertEqual(products_count,0)
