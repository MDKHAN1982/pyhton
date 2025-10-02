from django.db import models

# Create your models here.
class employee(models.Model):
    eno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=100)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=100)

def __str__(self):
    return 'Employee No: ' + str(self.eno) + ' Employee Name: ' + self.ename + ' Employee Salary: ' + str(self.esal) + ' Employee Address: ' + self.eaddr 
