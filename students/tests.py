from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student


class StudentApiTests(APITestCase):
	def test_student_crud_endpoints(self):
		response = self.client.post('/api/students/', {
			'name': 'Ada Lovelace',
			'age': 20,
			'course': 'Mathematics',
		}, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		student_id = response.data['id']

		response = self.client.get('/api/students/')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)

		response = self.client.put(f'/api/students/{student_id}/', {
			'name': 'Ada Lovelace',
			'age': 21,
			'course': 'Computer Science',
			'is_active': True,
		}, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

		response = self.client.patch(f'/api/students/{student_id}/', {
			'age': 22,
		}, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['age'], 22)

		response = self.client.delete(f'/api/students/{student_id}/')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertFalse(Student.objects.exists())

	def test_swagger_and_schema_are_available(self):
		self.assertEqual(self.client.get('/api/schema/').status_code, status.HTTP_200_OK)
		self.assertEqual(self.client.get('/api/docs/').status_code, status.HTTP_200_OK)
