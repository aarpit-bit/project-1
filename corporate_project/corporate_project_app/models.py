from django.db import models

### MADE COMPANY MODEL WITH ALL THE REQUIRED FIELDS SUCH AS COMPANY ID,NAME,DESCRIPTION,LOCATION,INDUSTRY,WEBSITE,COMPANY AGE,COMPANY NET WORTH,COMPANY FOUNDER,COMPANY HEADQUARTERS,COMPANY CEO,COMPANY EMPLOYEES,COMPANY PRODUCTS,COMPANY SERVICES,COMPANY MARKET CAP,COMPANY REVENUE,COMPANY PROFIT
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
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

### MADE EMPLOYEE MODEL WITH ALL THE REQUIRED FIELDS SUCH AS EMPLOYEE ID,NAME,AGE,GENDER,SALARY,COMPANY,DEPARTMENT,DATE OF BIRTH,JOINING DATE,PHONE NUMBER,EMAIL,ADDRESS
class Employee(models.Model):
    company_id=models.ForeignKey(Company,on_delete=models.CASCADE)
    employee_id=models.AutoField(primary_key=True)
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
    
### MADE PROJECT MODEL WITH ALL THE REQUIRED FIELDS SUCH AS PROJECT ID,NAME,DESCRIPTION,START DATE,END DATE,COMPANY,BUDGET,STATUS,DURATION

class Project(models.Model):
    name=models.CharField(max_length=255)
    company_id=models.ForeignKey(Company,on_delete=models.CASCADE)
    project_id=models.AutoField(primary_key=True)
    employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    description=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField()
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    budget=models.IntegerField()
    status=models.CharField(max_length=255)
    duration=models.IntegerField()


    def __str__(self):
        return self.name
