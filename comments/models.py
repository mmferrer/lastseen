from django.db import models
from accounts.models import UserAccount
from submissions.models import Submission
from datetime import date, time
import datetime

# Create your models here.
class Comment(models.Model):
	submission = models.ForeignKey(Submission)

	author = models.CharField(max_length = 30)
	title = models.CharField(max_length = 256)
	details = models.TextField()
	lastdate = models.DateField(default = date.today)
	lasttime = models.DateField(default = datetime.datetime.now())
	date = models.DateField(default = date.today)
	time = models.TimeField(default = datetime.datetime.now())
	latitude = models.FloatField()
	longitude = models.FloatField()
	address = models.CharField(max_length = 256)
