from django.test import TestCase

from .models import CheckInType, CheckIn

class CheckInTestCase(TestCase):
	def test_1(self):
		checkin_type = CheckInType.objects.create(
			title="1-week check-in",
			description="How's it going after 1 week?")

		checkin = CheckIn.objects.create(checkin_type=checkin_type)

		import ipdb; ipdb.set_trace()
