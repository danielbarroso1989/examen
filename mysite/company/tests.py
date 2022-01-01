from django.test import TestCase
from django.urls import reverse
from mysite.api.utils import search_symbol,validatedata

class CompanyTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def test_view_home(self):
        resp = self.client.get(reverse('home'), follow=True,
                               secure=True)
        self.assertTemplateUsed(resp, 'home.html')

    def test_view_create_form(self):
        resp = self.client.get(reverse('createform'), follow=True,
                               secure=True)
        self.assertTemplateUsed(resp, 'form.html')

    def test_view_list_form(self):
        resp = self.client.get(reverse('list_form'), follow=True,
                               secure=True)
        self.assertTemplateUsed(resp, 'list.html')

    def test_validate_symbol(self):
        ticker = "AA"
        ticker2 = "aa"
        _value = search_symbol("ohfejiofjvfojvovf")
        self.assertEqual(_value, False)

        _value2 = search_symbol(ticker)
        self.assertEqual(_value2["ticker"], ticker)

        _value3 = search_symbol(ticker2)
        self.assertEqual(_value3["ticker"], "AA")