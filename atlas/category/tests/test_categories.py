from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Category
from category.serializers import CategorySerializer


CATEGORY_URL = reverse('category:category-list')


class PublicCategorieAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_category_unauthorized(self):
        """Test that unauthenticated users can't retrieve category."""
        res = self.client.get(CATEGORY_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateCategorieAPITests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
        )
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )
        self.client = APIClient()

    def test_retrieve_category_admin(self):
        """Test that only admins can retrieve category."""
        Category.objects.create(name='Category 1')
        Category.objects.create(name='Category 2')

        self.client.force_authenticate(user=self.admin_user)
        res = self.client.get(CATEGORY_URL)

        category = Category.objects.all()
        serializer = CategorySerializer(Category, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_category_user_unauthorized(self):
        """Test that regular users cannot retrieve category."""
        Category.objects.create(name='Category 1')
        Category.objects.create(name='Category 2')

        self.client.force_authenticate(user=self.user)
        res = self.client.get(CATEGORY_URL)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_categorie_unauthorized(self):
        """Test that only admins can create categorY."""
        payload = {'name': 'New Category'}
        self.client.force_authenticate(user=self.user)
        res = self.client.post(CATEGORY_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_categorie_unauthorized(self):
        """Test that only admins can update category."""
        categorie = Category.objects.create(name='Category 1')
        payload = {'name': 'Updated Category'}

        self.client.force_authenticate(user=self.user)
        res = self.client.patch(
            reverse('category:category-detail',
                    args=[categorie.id]), payload)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_categorie_unauthorized(self):
        """Test that only admins can delete category."""
        categorie = Category.objects.create(name='Category 1')

        self.client.force_authenticate(user=self.user)
        res = self.client.delete(
            reverse('category:category-detail', args=[categorie.id]))

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)