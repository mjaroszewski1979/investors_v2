from django.shortcuts import render
from . import models
from django.views import View
from django.db.models import Q, Avg
from django.db.models.functions import ExtractYear
from django.utils import timezone
from datetime import date

class HomeView(View):
    def get(self, request):
        query_attributes = {}
        population_avg = int(models.Country.objects.aggregate(Avg('population'))['population__avg'])
        aum_avg = int(models.Fund.objects.aggregate(Avg('aum'))['aum__avg'])
        countries = models.Country.objects.all()
        funds = set(models.Fund.objects.values_list('market', flat=True))
        current_year = timezone.now().year
        age_avg = int(models.Investor.objects.aggregate(average_age=Avg(current_year - ExtractYear('age')))['average_age'])
        age_result = int(current_year - age_avg)
        date_value = date(year=age_result, month=1, day=1)
        country__name = request.GET.get('country-list', '')
        country__population = request.GET.get('population-avg', '')
        fund__aum = request.GET.get('aum-avg', '')
        age = request.GET.get('age-avg', '')

        if country__name:
            query_attributes['country__name'] = country__name
        fund__market = request.GET.get('market-list', '')
        if fund__market:
            query_attributes['fund__market'] = fund__market
        fund__long = request.GET.get('long-only', '')
        if fund__long:
            query_attributes['fund__long'] = True
        if country__population == 'above':
            query_attributes['country__population__gt'] = population_avg
        if country__population == 'below':
            query_attributes['country__population__lt'] = population_avg
        if fund__aum == 'above':
            query_attributes['fund__aum__gt'] = aum_avg
        if fund__aum == 'below':
            query_attributes['fund__aum__lt'] = aum_avg
        if age == 'above':
            query_attributes['age__gt'] = date_value
        if age == 'below':
            query_attributes['age__lt'] = date_value

        investors = models.Investor.objects.filter(**query_attributes)

        return render(request, 'index.html', locals())




