from django.db import models
from django.forms import TextInput, Textarea

class UserModel(models.Model):
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Employee(models.Model):  
    CATEGORY_CHOICES = [
        ('Complete', 'Complete'),
        ('On-Going', 'On-Going'),
        ('Under Procurement', 'Under Procurement'),
    ]

    SLIPPAGE_CHOICES = [
        ('ANS','ANS',),
        ('Negative','Negative'),
        ('Positive','Positive'),
        ('Pending','Pending'),
        ('Terminated','Terminated'),
        ('Blanks','Blanks')
    ]
    loc = models.CharField(max_length=1000)  
    title = models.CharField(max_length=1000, null=True, blank=True)
    desc = models.TextField(max_length=1000, null=True)  
    fund = models.TextField(max_length=1000, null=True)
    cont = models.TextField(max_length=1000, null=True)
    proj_profile = models.TextField()
    proj_stat = models.CharField(max_length=1000, choices=CATEGORY_CHOICES, null=True)
    proj_comment = models.TextField(max_length=1000)
    slip = models.CharField(max_length=1000, choices=SLIPPAGE_CHOICES, null=True)
    budg = models.IntegerField(max_length=1000, null=True) 
    agency = models.CharField(max_length=1000, null=True) 
    area = models.CharField(max_length=1000, null=True) 
    reg = models.CharField(max_length=1000, null=True) 
    cert = models.CharField(max_length=1000, null=True) 
    reco = models.CharField(max_length=1000, null=True)
    progress = models.IntegerField(null=True, default=0) 

    class Meta:  
        db_table = "employee"