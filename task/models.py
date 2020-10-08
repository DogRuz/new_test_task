from django.db import models

class Category(models.Model):
    title = models.CharField(null=True, blank=True, max_length=100)


class Company(models.Model):
    description = models.CharField(null=True, blank=True, max_length=5000)
    is_active = models.BooleanField(default=False)


class Product(models.Model):
    title = models.CharField(null=True, blank=True, max_length=100)
    description = models.CharField(null=True, blank=True, max_length=5000)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=False)