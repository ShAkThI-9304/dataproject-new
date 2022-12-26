from django.db import models
from django.contrib import admin

class bankdata(models.Model):
    class Meta():
        permissions = (("view_staff", "can view staff details."),
                 ("view_income", "can view income details"),
        ) 
    name_primary_key = models.CharField(max_length=30)
    pin = models.CharField(max_length=30)
    bank_account_num = models.IntegerField(primary_key=True,unique=True)
    contact_num = models.IntegerField()
    email = models.EmailField(max_length=50,unique=True)

class bankadmin(admin.ModelAdmin):
    list_display = ('name_primary_key', 'pin', 'bank_account_num', 'contact_num','email')