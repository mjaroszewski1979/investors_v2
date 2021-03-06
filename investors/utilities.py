from django.utils import timezone
from datetime import date

from django.db.models import Q, Avg
from django.db.models.functions import ExtractYear

from . import models

class QueryAttributes:
    def __init__(self):
        self.query_attributes = {}
        self.current_year = timezone.now().year
        self.all_investors = models.Investor.objects.all()
        self.all_countries = models.Country.objects.all()
        self.all_funds = models.Fund.objects.all()
        self.age_avg = int(self.all_investors.aggregate(average_age=Avg(self.current_year - ExtractYear('age')))['average_age'])
        self.population_avg = int(self.all_countries.aggregate(Avg('population'))['population__avg'])
        self.aum_avg = int(self.all_funds.aggregate(Avg('aum'))['aum__avg'])
        self.markets = self.all_funds.order_by('market').values_list('market', flat=True).distinct()
        self.age_result = int(self.current_year - self.age_avg)
        self.date_value = date(year=self.age_result, month=1, day=1)

    def get_query_attributes(self, country__name=None, fund__market=None, fund__long=None, country__population=None, fund__aum=None, age=None):
        if country__name:
            self.query_attributes['country__name'] = country__name
        if fund__market:
            self.query_attributes['fund__market'] = fund__market
        if fund__long:
            self.query_attributes['fund__long'] = True
        if country__population == 'above':
            self.query_attributes['country__population__gt'] = self.population_avg
        if country__population == 'below':
            self.query_attributes['country__population__lt'] = self.population_avg
        if fund__aum == 'above':
            self.query_attributes['fund__aum__gt'] = self.aum_avg
        if fund__aum == 'below':
            self.query_attributes['fund__aum__lt'] = self.aum_avg
        if age == 'above':
            self.query_attributes['age__gt'] = self.date_value
        if age == 'below':
            self.query_attributes['age__lt'] = self.date_value
        investors = self.all_investors.select_related('country', 'fund').all().filter(**self.query_attributes)
        return investors









