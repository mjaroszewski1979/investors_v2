from django.contrib import admin

from . import models

class InvestorsAdminArea(admin.AdminSite):
    site_header = 'Investors Admin Area'

investors_site = InvestorsAdminArea(name='InvestorsAdmin')

admin.site.register(models.Country)
admin.site.register(models.Fund)
admin.site.register(models.Investor)

investors_site.register(models.Country)
investors_site.register(models.Fund)
investors_site.register(models.Investor)
