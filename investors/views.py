# Import the render function to render templates
from django.shortcuts import render
# Import the View class for handling requests
from django.views import View

# Import local utilities and models modules
from . import utilities, models

class HomeView(View):
    """
    Class-based view to handle GET requests for the home page.
    Fetches and filters investor data based on query parameters.
    """
    
    def get(self, request):
        """
        Handle GET requests.
        Retrieves investor data and filters based on query parameters from the request.
        
        Args:
            request (HttpRequest): The request object containing query parameters.
        
        Returns:
            HttpResponse: The rendered template with context variables.
        """

        # Check if there are any investors in the database
        if models.Investor.objects.all().count() != 0:

            # Get query parameters from the request
            country__name = request.GET.get('country-list', '')
            country__population = request.GET.get('population-avg', '')
            fund__aum = request.GET.get('aum-avg', '')
            age = request.GET.get('age-avg', '')
            fund__market = request.GET.get('market-list', '')
            fund__long = request.GET.get('long-only', '')

            # Instantiate the QueryAttributes class
            data = utilities.QueryAttributes()

            # Get filtered investors based on query parameters
            investors = data.get_query_attributes(
                country__name=country__name, 
                fund__market=fund__market, 
                fund__long=fund__long, 
                country__population=country__population, 
                fund__aum=fund__aum, 
                age=age
            )

        # Render the 'index.html' template with the context variables
        return render(request, 'index.html', locals())




