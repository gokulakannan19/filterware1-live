from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('financial_accounting/', views.financial_accounting,
         name='financial_accounting'),
    path('financial_accounting/financial_accounting_questions/',
         views.financial_accounting_questions, name='upload_financial_accounting_questions'),
    path('financial_accounting/financial_accounting_answers/',
         views.financial_accounting_answers, name='upload_financial_accounting_answers'),

    path('auditing/', views.auditing, name='auditing'),
    path('auditing/auditing_questions/',
         views.auditing_questions, name='upload_auditing_questions'),
    path('auditing/auditing_answers/',
         views.auditing_answers, name='upload_auditing_answers'),

    path('management_accounting/', views.management_accounting,
         name='management_accounting'),
    path('management_accounting/management_accounting_questions/',
         views.management_accounting_questions, name='upload_management_accounting_questions'),
    path('management_accounting/management_accounting_answers/',
         views.management_accounting_answers, name='upload_management_accounting_answers'),

    path('company_law/', views.company_law,
         name='company_law'),
    path('company_law/company_law_questions/',
         views.company_law_questions, name='upload_company_law_questions'),
    path('company_law/company_law_answers/',
         views.company_law_answers, name='upload_company_law_answers'),

    path('service_marketing/', views.service_marketing,
         name='service_marketing'),
    path('service_marketing/service_marketing_questions/',
         views.service_marketing_questions, name='upload_service_marketing_questions'),
    path('service_marketing/service_marketing_answers/',
         views.service_marketing_answers, name='upload_service_marketing_answers'),

    path('retail_marketing/', views.retail_marketing,
         name='retail_marketing'),
    path('retail_marketing/retail_marketing_questions/',
         views.retail_marketing_questions, name='upload_retail_marketing_questions'),
    path('retail_marketing/retail_marketing_answers/',
         views.retail_marketing_answers, name='upload_retail_marketing_answers')


]