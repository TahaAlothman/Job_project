from django.db import models

# Create your models here.

Category_CHOICES = (('All Category','All Category'),('Category 1','Category 1'),('Category 2','Category 2'),('Category 3','Category 3'),('Category 4','Category 4') )
Job_Type_Choices=(('Full Time','Full Time'),('Part Time','Part Time'),('Remote','Remote'),('Freelance','Freelance'))
Experience_Choices = (('1-2 Years','1-2 Years'),('2-3 Years','2-3 Years'),('3-6 Years','3-6 Years'),('6-more','6-more'))
PostedTime_Choices = (('Any','Any'),('Today','Today'),('Last 2 days','Last 2 days'),('Last 3 days','Last 3 days'),('Last 5 days','Last 5 days'),('Last 10 days','Last 10 days'))
class Job (models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='job')
    job_locetion = models.CharField(max_length=100)
    agency = models.CharField(max_length=100)
    rounding_salary = models.CharField(max_length=100)
    job_Description =models.TextField(max_length=10000)
    repuired_knowledge = models.TextField(max_length=10000)
    experience = models.TextField(max_length=10000)
    overview = models.OneToOneField('Job_Overview',related_name='job_overview',on_delete=models.CASCADE)
    company = models.ForeignKey('Company',related_name='job_company',on_delete=models.CASCADE)
    job_Art = models.ForeignKey('Category',related_name='category_job',on_delete=models.CASCADE)




class Job_Overview(models.Model):
    ## job = models.OneToOneField(Job,related_name='job_overview',on_delete=models.CASCADE)
    Posted_date = models.DateTimeField()
    locetion = models.CharField(max_length=50)
    Vacancy = models.IntegerField()
    job_natur = models.ForeignKey(Job,related_name='job_time',on_delete=models.CASCADE)
    salary = models.CharField(max_length=100)
    Application_date = models.CharField(max_length=100)

class Company(models.Model):
    name = models.CharField(max_length=50)
    subtitle = models.TextField(max_length=1000)
    web_site = models.CharField(max_length=100)
    email = models.CharField(max_length=100)



class Category (models.Model):
    logo =  models.ImageField(upload_to='logo')
    name = models.CharField(max_length=120)
    count = models.IntegerField()
   # jobs = models.ForeignKey(Job,related_name='category_job',on_delete=models.CASCADE)
    job_category = models.CharField(max_length=15,choices=Category_CHOICES)
    job_type = models.CharField(max_length=15,choices=Job_Type_Choices)
    job_location =  models.CharField(max_length=15,choices=Category_CHOICES)
    Experience = models.CharField(max_length=100,choices=Experience_Choices)
    Posted_Within = models.CharField(max_length=100,choices=PostedTime_Choices)


