from django.shortcuts import render
from . import models
from django.views import View
from django.db.models import Q, Avg

class HomeView(View):
    def get(self, request):
        average = int(models.Country.objects.aggregate(Avg('population'))['population__avg'])
        countries = models.Country.objects.all()
        funds = set(models.Fund.objects.values_list('market', flat=True))
        population = request.GET.get('population-avg')
        result = request.GET.get('country-list')
        market = request.GET.get('market-list')
        long = request.GET.get('long-only')
        if long != None and result and market and population == 'above':
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
            investors = models.Investor.objects.filter(Q(country__population__lt=average))
        
        return render(request, 'index.html', locals())




