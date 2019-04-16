from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient

from dynamic_model_fields.apps.insurance.models import FieldType


class BaseTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        field_type1 = FieldType(name="Integer")
        field_type2 = FieldType(name="Text")

        field_type1.save()
        field_type2.save()

        self.valid_risk_type_data = {
            "name": "Prize Policy",
            "description": "This is my description feild which can not be empty",
            "fields": [
                {
                    "name": "first_name",
                    "field_type": str(field_type1.id)
                },
                {
                    "name": "last_name",
                    "field_type": str(field_type2.id)
                }
            ]
        }

    def create_risk_type(self, data):
        return self.client.post(
            reverse('list_create_views'),
            data=data, format='json')
