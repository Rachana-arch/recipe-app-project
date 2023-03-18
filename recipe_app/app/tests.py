from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
# Create your tests here.

TOKEN_URL = reverse('app:token')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserAPITest(TestCase):

    def set_up(self):
        self.client = APIClient()

    def test_create_token_for_user(self):
        user_details = {
            'email': 'test@example.com',
            'name': 'test name',
             'password': 'test123'}
        create_user(**user_details)
        print("User creation done")
        payload = {'email': user_details['email'],
                   'password': user_details['password']}
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn(res.status_code, status.HTTP_200_OK)
        self.assertEqual('token', res.data)

    def test_create_token_bad_credential(self):
        create_user(email='test@example.com', password='test123')
        payload ={'email':'test@example.com', 'password':'badpass'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', res.data)

    def test_create_token_blank_credential(self):
        # create_user(email='test@example.com', password='Test123')
        payload = {'email': 'test@example.com', 'password': ''}
        res = self.client.post(TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', res.data)