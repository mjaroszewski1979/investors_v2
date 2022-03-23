from django.urls import reverse, resolve
from django.test import TestCase, Client
from . import views, models, utilities



class CatalogTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.country_1 = models.Country(name='united states', population=300000000)
        self.country_1.save()
        self.country_2 = models.Country(name='france', population=50000000)
        self.country_2.save()
        self.fund_1 = models.Fund(name='the vanguard group', aum=300000000, long=True, market='stocks')
        self.fund_1.save()
        self.fund_2 = models.Fund(name='sesamm', aum=100000000, long=False, market='bonds')
        self.fund_2.save()
        self.investor_1 = models.Investor(name='MORTIMER J. BUCKLEY', age='1990-10-10', country=self.country_1, fund=self.fund_1)
        self.investor_1.save()
        self.investor_2 = models.Investor(name='MICHEL MORVAN', age='1980-10-10', country=self.country_2, fund=self.fund_2)
        self.investor_2.save()

       



    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class, views.HomeView)

    def test_index_get(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Famous Investors', status_code=200)
        self.assertTemplateUsed(response, 'index.html')

    def test_uitilities(self):
        data = utilities.QueryAttributes()
        self.assertEquals(data.population_avg, 175000000)
        self.assertEquals(data.age_avg, 37)
        self.assertEquals(data.aum_avg, 200000000)
        self.assertEquals(data.funds[0], 'bonds')


