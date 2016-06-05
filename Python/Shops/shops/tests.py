from django.test import TestCase
import unittest
from models import Shop, Provider

# Create your tests here.

class DBTestCase(unittest.TestCase):
    def setUp(self):
        self.t1 = Shop.objects.create(name="Sklep", owner="Czlowiek", address="losowa 12", phone="123456789")
        self.t2 = Provider.objects.create(name="Andrzej Miesny", product = "mieso", phone="987654321", shop="Sklep")

    def tearDown(self):
        self.t2.delete()
        self.t1.delete()

