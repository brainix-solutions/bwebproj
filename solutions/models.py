from django.db import models

# Create your models here.
class Trialworkshop(models.Model):
    CATEGORY = (
        ('male', 'male'),
        ('female', 'female' ),
    )
    CATEGORY1 = (
        ('1:1', '1:1'),
        ('1:5', '1:5' ),
    )
    CATEGORY2 = (
        ('English', 'English'),
        ('Tamil', 'Tamil' ),
        ('Malayalam', 'Malayalam'),
    )
    fname = models.CharField(max_length=200, null=True)
    lname = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, choices = CATEGORY)
    pname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phno = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    spref = models.CharField(max_length=200, null=True, choices = CATEGORY1)
    lpref = models.CharField(max_length=200, null=True, choices = CATEGORY2)

    def __str__(self):
               return self.fname

class Payworkshop(models.Model):
    CATEGORY = (
        ('male', 'male'),
        ('female', 'female' ),
    )
    CATEGORY1 = (
        ('1:1', '1:1'),
        ('1:5', '1:5' ),
    )
    CATEGORY2 = (
        ('English', 'English'),
        ('Tamil', 'Tamil' ),
        ('Malayalam', 'Malayalam'),
    )
    fname = models.CharField(max_length=200, null=True)
    lname = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, choices = CATEGORY)
    pname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phno = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    spref = models.CharField(max_length=200, null=True, choices = CATEGORY1)
    lpref = models.CharField(max_length=200, null=True, choices = CATEGORY2)
    razorpay_id = models.CharField(max_length=200, null=True)
    id = models.IntegerField(primary_key=True)
    order_id = models.CharField(max_length=200, null=True)
    paid = models.BooleanField(default=False)
    def __str__(self):
               return self.fname

class Feedbackform(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    message = models.CharField(max_length=200, null=True)
    
    def __str__(self):
               return self.name
