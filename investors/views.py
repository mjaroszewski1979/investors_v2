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
        pop_avg = int(models.Country.objects.aggregate(Avg('population'))['population__avg'])
        aum_avg = int(models.Fund.objects.aggregate(Avg('aum'))['aum__avg'])
        countries = models.Country.objects.all()
        funds = set(models.Fund.objects.values_list('market', flat=True))
        current_year = timezone.now().year
        age_avg = int(models.Investor.objects.aggregate(average_age=Avg(current_year - ExtractYear('age')))['average_age'])
        age_result = int(current_year - age_avg)
        date_val = date(year=age_result, month=1, day=1)
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
            query_attributes['country__population__gt'] = pop_avg
        if country__population == 'below':
            query_attributes['country__population__lt'] = pop_avg
        if fund__aum == 'above':
            query_attributes['fund__aum__gt'] = aum_avg
        if fund__aum == 'below':
            query_attributes['fund__aum__lt'] = aum_avg
        if age == 'above':
            query_attributes['age__gt'] = date_val
        if age == 'below':
            query_attributes['age__lt'] = date_val
        '''if long != None and result and market and population == 'above':
            investors = models.Investor.objects.filter(Q(fund__long=True) & Q(country__name=result) & Q(fund__market=market) & Q(country__population__gt=average))
        elif long != None and result and market:
            investors = models.Investor.objects.filter(Q(fund__long=True) & Q(country__name=result) & Q(fund__market=market) & Q(country__population__gt=average))
        elif long != None and result and population == 'above':
            investors = models.Investor.objects.filter(Q(fund__long=True) & Q(country__name=result) & Q(country__population__gt=average))
        elif long != None and result:
            investors = models.Investor.objects.filter(Q(fund__long=True) & Q(country__name=result))
        elif long != None and market and population == 'above':
            investors = models.Investor.objects.filter(Q(fund__long=True) & Q(fund__market=market) & Q(country__population__gt=average))
        elif long != None and market:
            investors = models.Investor.objects.filter(Q(fund__long=True) & Q(fund__market=market))
        elif result and market and population == 'above':
            investors = models.Investor.objects.filter(Q(country__name=result) & Q(fund__market=market) & Q(country__population__gt=average))
        elif result and market:
            investors = models.Investor.objects.filter(Q(country__name=result) & Q(fund__market=market))
        elif long != None and population == 'above':
            investors = models.Investor.objects.filter(Q(fund__long=True) & Q(country__population__gt=average))
        elif long != None:
            investors = models.Investor.objects.filter(Q(fund__long=True))
        elif result and population == 'above':
            investors = models.Investor.objects.filter(Q(country__name=result) & Q(country__population__gt=average))
        elif result:
            investors = models.Investor.objects.filter(Q(country__name=result))
        elif market and population == 'above':
            investors = models.Investor.objects.filter(Q(fund__market=market) & Q(country__population__gt=average))
        elif market:
            investors = models.Investor.objects.filter(Q(fund__market=market))
        elif population == 'above':
            investors = models.Investor.objects.filter(Q(country__population__gt=average))
        elif long != None and result and market and population == 'below':
            investors = models.Investor.objects.filter(Q(fund__long=True) & Q(country__name=result) & Q(fund__market=market) & Q(country__population__lt=average))
        elif long != None and result and market:
            investors = models.Investor.objects.filter(Q(fund__long=True) & Q(country__name=result) & Q(fund__market=market) & Q(country__population__lt=average))
        elif long != None and result and population == 'below':
            investors = models.Investor.objects.filter(Q(fund__long=True) & Q(country__name=result) & Q(country__population__lt=average))
        elif long != None and result:
            investors = models.Investor.objects.filter(Q(fund__long=True) & Q(country__name=result))
        elif long != None and market and population == 'below':
            investors = models.Investor.objects.filter(Q(fund__long=True) & Q(fund__market=market) & Q(country__population__lt=average))
        elif long != None and market:
            investors = models.Investor.objects.filter(Q(fund__long=True) & Q(fund__market=market))
        elif result and market and population == 'below':
            investors = models.Investor.objects.filter(Q(country__name=result) & Q(fund__market=market) & Q(country__population__lt=average))
        elif result and market:
            investors = models.Investor.objects.filter(Q(country__name=result) & Q(fund__market=market))
        elif long != None and population == 'below':
            investors = models.Investor.objects.filter(Q(fund__long=True) & Q(country__population__lt=average))
        elif long != None:
            investors = models.Investor.objects.filter(Q(fund__long=True))
        elif result and population == 'below':
            investors = models.Investor.objects.filter(Q(country__name=result) & Q(country__population__lt=average))
        elif result:
            investors = models.Investor.objects.filter(Q(country__name=result))
        elif market and population == 'below':
            investors = models.Investor.objects.filter(Q(fund__market=market) & Q(country__population__lt=average))
        elif market:
            investors = models.Investor.objects.filter(Q(fund__market=market))
        elif population == 'below':
            investors = models.Investor.objects.filter(Q(country__population__lt=average))'''

        investors = models.Investor.objects.filter(**query_attributes)

        return render(request, 'index.html', locals())




