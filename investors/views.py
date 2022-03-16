from django.shortcuts import render
from . import models
from django.views import View
from django.db.models import Q

class HomeView(View):
    def get(self, request):
        countries = models.Country.objects.all()
        funds = set(models.Fund.objects.values_list('market', flat=True))
        result = request.GET.get('country-list')
        market = request.GET.get('market-list')
        if request.GET.get('long-only') != None:
            long = 1
            investors = models.Investor.objects.filter(Q(country__name=result) & Q(fund__long=long) & Q(fund__market=market))
        else:
            investors = models.Investor.objects.filter(Q(country__name=result) & Q(fund__market=market))
        
        return render(request, 'index.html', locals())




