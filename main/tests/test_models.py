from decimal import Decimal
from django.test import TestCase
from main.models import Product

class TestModel(TestCase):

    def test_active_manager_works(self):

        Product.objects.create(
            name  = 'Test Book A',
            price = Decimal("10.00")
        )
        Product.objects.create(
            name  = 'Test Book B',
            price = Decimal("5.00")
        )
        Product.objects.create(
            name   = 'Test Book C',
            price  = Decimal("15.00"),
            active = False
        )

        self.assertEqual(len(Product.objects.active()), 2)