from .test_data import missing_field_risk_type_data, invalid_risk_type_data
from django.urls import reverse

from rest_framework import status

from .import BaseTest

from .factories.insurance_factory import RiskTypeFactory


class TestRiskType(BaseTest):

    def test_list_risk_types_succeeds(self):

        RiskTypeFactory.create_batch(5)
        response = self.client.get(
            reverse('list_create_views'),
            format='json')
        self.assertEqual(len(response.data['results']), 5)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_risk_type_succeeds(self):

        risk_type = RiskTypeFactory()

        response = self.client.get(
            reverse('update_retrieve_destroy', args=(risk_type.id,)),
            format='json')
        self.assertEqual(response.data['id'], str(risk_type.id))
        self.assertEqual(response.data['name'], risk_type.name)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_with_valid_data_succeeds(self):

        response = self.create_risk_type(self.valid_risk_type_data)
        self.assertEqual(response.data['name'],
                         self.valid_risk_type_data['name'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_with_invalid_data_fails(self):

        response = self.create_risk_type(invalid_risk_type_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_with_missing_fields_fails(self):

        response = self.create_risk_type(missing_field_risk_type_data)
        self.assertEqual(response.data.get('errors')[
                         'fields'][0], 'fields can not be empty')
        self.assertEqual(response.data.get('errors')[
                         'name'][0], 'This field is required.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
