from django.db import models
from django.core.urlresolvers import reverse

from accounts.models import UserAccount

# Create your models here.
class Submission(models.Model):
	user = models.ForeignKey(UserAccount)
	submission_date = models.DateTimeField('submission date')
	latitude = models.FloatField()
	longitude = models.FloatField()
	found = models.BooleanField(default=False)
	details = models.TextField()

	def __str__(self):
		return ' '.join([
				self.latitude,
				self.longitude,
			])

	def get_absolute_url(self):
		return reverse('submission-view', kwags={'pk': self.id})

	def __unicode__(self):
		return self.details

	def was_found(self):
		return self.found

	was_found.admin_order_field = 'found'
	was_found.admin_order_field = True
	was_found.short_description = 'Found'

class Comment(models.Model):
	user = models.ForeignKey(UserAccount)
	submission = models.ForeignKey(Submission)
	latitude = models.FloatField()
	longitude = models.FloatField()
	details = models.TextField()

	def __unicode__(self):
		return self.details