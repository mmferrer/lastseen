from django.contrib.auth.models import User, UserManager
from django.db import models
from datetime import datetime

# Create your models here.
class UserAccount(User):
	GENDER_CHOICES=(('m', 'Male'),('f','Female'))  

	gender=models.CharField(max_length = 10, choices = GENDER_CHOICES, default = 'm')
	birthday=models.DateField(default = datetime.now())
	address=models.CharField(max_length = 30, blank = True)
	facebook=models.EmailField(max_length = 30, blank = True)
	twitter=models.CharField(max_length = 20, blank = True)
	emailcode=models.CharField(max_length = 10)
    # slug = models.SlugField(max_length=100, unique=True, null=True)
	#active =  models.BooleanField()

class Badge(models.Model):
	user = models.ForeignKey(UserAccount)
	reputation = models.FloatField()
	badge = models.CharField(max_length=100)