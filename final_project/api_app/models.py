from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Employee(models.Model):
    employee_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=10)
    hire_date = models.CharField(max_length=10)
    job_id = models.CharField(max_length=100)
    salary = models.IntegerField()
    commission_pct = models.IntegerField()
    manager_id = models.IntegerField()
    department_id = models.IntegerField()
    image = models.ImageField(default=None, blank=True)


    def __str__(self):
        employee_name = self.first_name + " " + self.last_name
        return employee_name