# Import date class from datetime module
from datetime import date

# Import Django's timezone utility
from django.utils import timezone
# Import Q and Avg for query construction and aggregation
from django.db.models import Q, Avg
# Import ExtractYear for extracting year from date field
from django.db.models.functions import ExtractYear

# Import local models module
from . import models

class QueryAttributes:
    """
    Class to encapsulate query attributes for filtering investors based on various criteria.
    Initializes with aggregate data from all investors, countries, and funds.
    """
    
    def __init__(self):
        """
        Initialize the QueryAttributes class.
        Aggregates average age of investors, average population of countries, and average AUM of funds.
        Also prepares distinct market values and calculates date value for age comparison.
        """

        # Initialize an empty dictionary for query attributes
        self.query_attributes = {}
        
        # Get the current year
        self.current_year = timezone.now().year
        
        # Fetch all investor records
        self.all_investors = models.Investor.objects.all()
        
        # Fetch all country records
        self.all_countries = models.Country.objects.all()
        
        # Fetch all fund records
        self.all_funds = models.Fund.objects.all()

        # Calculate average age of investors
        self.age_avg = int(self.all_investors.aggregate(average_age=Avg(self.current_year - ExtractYear('age')))['average_age'])
        
        # Calculate average population of countries
        self.population_avg = int(self.all_countries.aggregate(Avg('population'))['population__avg'])
        
        # Calculate average assets under management (AUM) of funds
        self.aum_avg = int(self.all_funds.aggregate(Avg('aum'))['aum__avg'])
        
        # Get distinct market values from funds
        self.markets = self.all_funds.order_by('market').values_list('market', flat=True).distinct()
        
        # Calculate date value for age comparison
        self.age_result = int(self.current_year - self.age_avg)
        
        # Create a date object for the calculated age
        self.date_value = date(year=self.age_result, month=1, day=1)

    def get_query_attributes(self, country__name=None, fund__market=None, fund__long=None, country__population=None, fund__aum=None, age=None):
        """
        Prepare the query attributes for filtering investors based on provided criteria.
        
        Args:
            country__name (str, optional): Name of the country to filter by.
            fund__market (str, optional): Market type of the fund to filter by.
            fund__long (bool, optional): Whether to filter funds that are long.
            country__population (str, optional): Filter by country population ('above' or 'below' average).
            fund__aum (str, optional): Filter by fund AUM ('above' or 'below' average).
            age (str, optional): Filter by investor age ('above' or 'below' average).
        
        Returns:
            QuerySet: A queryset of investors filtered based on the provided criteria.
        """

        # Add country name to query attributes if provided
        if country__name:
            self.query_attributes['country__name'] = country__name
        
        # Add fund market to query attributes if provided   
        if fund__market:
            self.query_attributes['fund__market'] = fund__market
       
        # Add fund long status to query attributes if provided
        if fund__long:
            self.query_attributes['fund__long'] = True
       
        # Add population filter to query attributes if provided
        if country__population == 'above':
            self.query_attributes['country__population__gt'] = self.population_avg
        if country__population == 'below':
            self.query_attributes['country__population__lt'] = self.population_avg
        
        # Add AUM filter to query attributes if provided
        if fund__aum == 'above':
            self.query_attributes['fund__aum__gt'] = self.aum_avg
        if fund__aum == 'below':
            self.query_attributes['fund__aum__lt'] = self.aum_avg
        
        # Add age filter to query attributes if provided
        if age == 'above':
            self.query_attributes['age__gt'] = self.date_value
        if age == 'below':
            self.query_attributes['age__lt'] = self.date_value
        
        # Fetch investors filtered by the constructed query attributes
        investors = self.all_investors.select_related('country', 'fund').all().filter(**self.query_attributes)
        return investors









