import django_filters
from django_filters import CharFilter

from . models import FinancialAccounting, Auditing, ManagementAccounting, CompanyLaw, ServiceMarketing, RetailMarketing


class FinancialAccountingFilter(django_filters.FilterSet):
    question = CharFilter(field_name="question", lookup_expr='icontains')
    answer = CharFilter(field_name="answer", lookup_expr='icontains')
    s_no = CharFilter(field_name="s_no", lookup_expr='icontains')

    class Meta:
        model = FinancialAccounting
        fields = '__all__'


class AuditingFilter(django_filters.FilterSet):
    question = CharFilter(field_name="question", lookup_expr='icontains')
    answer = CharFilter(field_name="answer", lookup_expr='icontains')
    s_no = CharFilter(field_name="s_no", lookup_expr='icontains')

    class Meta:
        model = Auditing
        fields = '__all__'


class ManagementAccountingFilter(django_filters.FilterSet):
    question = CharFilter(field_name="question", lookup_expr='icontains')
    answer = CharFilter(field_name="answer", lookup_expr='icontains')
    s_no = CharFilter(field_name="s_no", lookup_expr='icontains')

    class Meta:
        model = ManagementAccounting
        fields = '__all__'


class CompanyLawFilter(django_filters.FilterSet):
    question = CharFilter(field_name="question", lookup_expr='icontains')
    answer = CharFilter(field_name="answer", lookup_expr='icontains')
    s_no = CharFilter(field_name="s_no", lookup_expr='icontains')

    class Meta:
        model = CompanyLaw
        fields = '__all__'


class ServiceMarketingFilter(django_filters.FilterSet):
    question = CharFilter(field_name="question", lookup_expr='icontains')
    answer = CharFilter(field_name="answer", lookup_expr='icontains')
    s_no = CharFilter(field_name="s_no", lookup_expr='icontains')

    class Meta:
        model = ServiceMarketing
        fields = '__all__'


class RetailMarketingFilter(django_filters.FilterSet):
    question = CharFilter(field_name="question", lookup_expr='icontains')
    answer = CharFilter(field_name="answer", lookup_expr='icontains')
    s_no = CharFilter(field_name="s_no", lookup_expr='icontains')

    class Meta:
        model = RetailMarketing
        fields = '__all__'