from django.test import TestCase
from rest_framework.test import APITestCase,RequestsClient

from django.contrib.auth.models import User

from api.models import Account, Review
# Create your tests here.
#
# class ReviewTest(APITestCase):
#     fixtures = ['auth_user_json']