from django.contrib import admin
from company.models import Company
# Register your models here.
@admin.register(Company)
class Subscriptions_idm_online(admin.ModelAdmin):
    pass