from django.test import TestCase
from .models import UPSOption

class UPSTestCase(TestCase):
    def setUp(self):
        UPSOption.objects.create(name="Standard Shipping", description="Delivery within 5-7 business days.", price=10.00)
        UPSOption.objects.create(name="Express Shipping", description="Delivery within 1-2 business days.", price=25.00)

    def test_ups_options(self):
        standard = UPSOption.objects.get(name="Standard Shipping")
        express = UPSOption.objects.get(name="Express Shipping")
        self.assertEqual(standard.description, "Delivery within 5-7 business days.")
        self.assertEqual(standard.price, 10.00)
        self.assertEqual(express.description, "Delivery within 1-2 business days.")
        self.assertEqual(express.price, 25.00)