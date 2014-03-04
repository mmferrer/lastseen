from django.db import models
from accounts.models import UserAccount
from datetime import date, time
import datetime

# Create your models here.
class Submission(models.Model):
	FOUND_CHOICES=(('y', 'Yes'),('n','No'))

	author = models.CharField(max_length = 30)
	title = models.CharField(max_length = 256)
	details = models.TextField()
	lastdate = models.DateField(default = date.today)
	lasttime = models.DateField(default = datetime.datetime.now())
	date = models.DateField(default = date.today)
	time = models.TimeField(default = datetime.datetime.now())
	# photo = models.ImageField(upload_to = 'image/submissions/photo', null = True, default = 'image/notes/default.jpg')
	found = models.CharField(max_length = 10, choices = FOUND_CHOICES, default = 'n')
	views = models.IntegerField(default = 0, blank = True, null = True)
	latitude = models.FloatField()
	longitude = models.FloatField()
	address = models.CharField(max_length = 256)