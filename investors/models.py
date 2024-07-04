from django.db import models

class BaseClass(models.Model):
    """
    Abstract base model that includes a name field.
    This model will not be created in the database.
    """
    name = models.CharField(max_length=100)

    class Meta:
        """
        Metadata options for the BaseClass.
        Sets this model as abstract and orders by the name field.
        """
        abstract = True
        ordering = ['name']

    def __str__(self):
        """
        Return the string representation of the BaseClass.
        This method returns the name of the instance.
        """
        return self.name

class Country(BaseClass):
    """
    Model representing a country.
    Inherits from BaseClass and adds a population field.
    """
    population = models.PositiveIntegerField()

class Fund(BaseClass):
    """
    Model representing a financial fund.
    Inherits from BaseClass and adds fields for AUM, long/short position, and market.
    """
    aum = models.PositiveIntegerField()
    long = models.BooleanField()
    market = models.CharField(max_length=100)

class Investor(BaseClass):
    """
    Model representing an investor.
    Inherits from BaseClass and adds fields for age, country, and fund.
    """
    age = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    fund = models.ForeignKey(Fund, null=True, on_delete=models.CASCADE)

    def get_age(self):
         """
        Return the birth year of the investor.
        This method extracts and returns the year part from the age field.
        """
        return self.age.year


