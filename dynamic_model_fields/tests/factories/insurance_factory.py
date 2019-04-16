import factory
from faker import Factory

from dynamic_model_fields.apps.insurance.models import FieldType, Field, RiskType

faker = Factory.create()

class FieldTypeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = FieldType

    name = factory.LazyAttribute(lambda _: faker.text(80))


class FieldFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Field

    name = factory.LazyAttribute(lambda _: faker.text(50))
    field_type = factory.SubFactory(FieldTypeFactory)
    options = factory.Iterator([[faker.text(50)]])


class RiskTypeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = RiskType

    name = factory.LazyAttribute(lambda _: faker.text(80))
    description = factory.LazyAttribute(lambda _: faker.text(128))

    @factory.post_generation
    def fields(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for field in extracted:
                self.fields.add(field)
