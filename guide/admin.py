from django.contrib import admin
from . models import FinancialAccounting, Auditing, ManagementAccounting, CompanyLaw, ServiceMarketing, RetailMarketing

# Register your models here.


class FinancialAccountingAdmin(admin.ModelAdmin):
    list_display = ('s_no', 'question', 'answer')


admin.site.register(FinancialAccounting, FinancialAccountingAdmin)


class AuditingAdmin(admin.ModelAdmin):
    list_display = ('s_no', 'question', 'answer')


admin.site.register(Auditing, AuditingAdmin)


class ManagementAccountingAdmin(admin.ModelAdmin):
    list_display = ('s_no', 'question', 'answer')


admin.site.register(ManagementAccounting, ManagementAccountingAdmin)


class ServiceMarketingAdmin(admin.ModelAdmin):
    list_display = ('s_no', 'question', 'answer')


admin.site.register(ServiceMarketing, ServiceMarketingAdmin)


class CompanyLawAdmin(admin.ModelAdmin):
    list_display = ('s_no', 'question', 'answer')


admin.site.register(CompanyLaw, CompanyLawAdmin)


class RetailMarketingAdmin(admin.ModelAdmin):
    list_display = ('s_no', 'question', 'answer')


admin.site.register(RetailMarketing, RetailMarketingAdmin)