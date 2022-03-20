from django.shortcuts import render
from django.views import View

from . import utilities

class HomeView(View):
    def get(self, request):
        country__name = request.GET.get('country-list', '')
        country__population = request.GET.get('population-avg', '')
        fund__aum = request.GET.get('aum-avg', '')
        age = request.GET.get('age-avg', '')
        fund__market = request.GET.get('market-list', '')
        fund__long = request.GET.get('long-only', '')
        data = utilities.QueryAttributes()
        investors = data.get_query_attributes(country__name=country__name, fund__market=fund__market, fund__long=fund__long, country__population=country__population, fund__aum=fund__aum, age=age)

        return render(request, 'index.html', locals())




