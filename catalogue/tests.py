from django.test import TestCase
from .models import Catalogue

# Create your tests here.
class CatalogueTest(TestCase):
    """ Testing catalogue models functionality """

    def test_str(self):
        test_name = Catalogue(name='A catalogue entry')
        self.assertEqual(str(test_name), 'A catalogue entry')