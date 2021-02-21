from django.db import models


# Create your models here.
class FinancialAccounting(models.Model):
    s_no = models.PositiveSmallIntegerField(null=True)
    question = models.CharField(max_length=500, null=True)
    answer = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.question


class Auditing(models.Model):
    s_no = models.PositiveSmallIntegerField(null=True)
    question = models.CharField(max_length=500, null=True)
    answer = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.question


class ManagementAccounting(models.Model):
    s_no = models.PositiveSmallIntegerField(null=True)
    question = models.CharField(max_length=500, null=True)
    answer = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.question


class CompanyLaw(models.Model):
    s_no = models.PositiveSmallIntegerField(null=True)
    question = models.CharField(max_length=500, null=True)
    answer = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.question


class ServiceMarketing(models.Model):
    s_no = models.PositiveSmallIntegerField(null=True)
    question = models.CharField(max_length=500, null=True)
    answer = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.question


class RetailMarketing(models.Model):
    s_no = models.PositiveSmallIntegerField(null=True)
    question = models.CharField(max_length=500, null=True)
    answer = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.question