from django.db import models
class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    website = models.URLField(max_length=255)
    company_age = models.IntegerField()
    company_net_worth = models.IntegerField()
    company_founder = models.CharField(max_length=255)
    company_headquarters = models.CharField(max_length=255)
    company_ceo = models.CharField(max_length=255)
    company_employees = models.IntegerField()
    company_products = models.CharField(max_length=255)
    company_services = models.CharField(max_length=255)
    company_market_cap = models.IntegerField()
    company_revenue = models.IntegerField()
    company_profit = models.IntegerField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=255)
    salary = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.CharField(max_length=255)
    date_of_birth=models.DateField()
    joining_date=models.DateField()
    phone_number=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    address=models.TextField()

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField()
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    budget=models.IntegerField()
    status=models.CharField(max_length=255)
    duration=models.IntegerField()
    

    def __str__(self):
        return self.name
