from django.urls import reverse

from rest_framework import status

from .import BaseTest

from .factories.insurance_factory import FieldTypeFactory


class TestFieldType(BaseTest):

    def test_list_field_types_succeeds(self):

        FieldTypeFactory.create_batch(5)
        response = self.client.get(
            reverse('field-types-list_view'),
            format='json')
        self.assertGreater(len(response.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
