from django.db import models

# Create your models here.

Category_CHOICES = (('All Category','All Category'),('Category 1','Category 1'),('Category 2','Category 2'),('Category 3','Category 3'),('Category 4','Category 4') )
Job_Type_Choices=(('Full Time','Full Time'),('Part Time','Part Time'),('Remote','Remote'),('Freelance','Freelance'))
class Job (models.Model):  #api list detail update create
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='job')
    job_locetion = models.CharField(max_length=100)
    agency = models.CharField(max_length=100)
    rounding_salary = models.CharField(max_length=100)
    job_Description =models.TextField(max_length=10000)
    
    Experience = models.TextField(max_length=10000)
    company = models.ForeignKey('Company',related_name='job_company',on_delete=models.CASCADE)
    job_natur= models.CharField(max_length=100,choices=Job_Type_Choices)
    Vacancy = models.IntegerField()
    salary_year = models.CharField(max_length=100)
   
    def __str__(self):
        return self.name





class Company(models.Model):
    name = models.CharField(max_length=50)
    subtitle = models.TextField(max_length=1000)
    web_site = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category (models.Model):
    logo =  models.ImageField(upload_to='logo')
    name = models.CharField(max_length=120)
  

    def __str__(self):
        return self.name
