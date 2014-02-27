from django.test import TestCase
from models import Submission

# Create your tests here.
class SubmissionTests(TestCase):
	def test_str(self):
		submission = Submission(latitude='10.9', longitude='0.8')

		self.assertEquals(
			str(submission),
			'10.9 0.8',
		)