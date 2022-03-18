from django.db import models

class BaseClass(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name

class Country(BaseClass):
    population = models.PositiveIntegerField()

class Fund(BaseClass):
    aum = models.PositiveIntegerField()
    long = models.BooleanField()
    market = models.CharField(max_length=100)

class Investor(BaseClass):
    age = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    fund = models.ForeignKey(Fund, null=True, on_delete=models.CASCADE)

    def get_age(self):
        return self.age.year


