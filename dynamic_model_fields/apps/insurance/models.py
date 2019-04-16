from uuid import uuid4

from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FieldType(BaseModel):

    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class Field(BaseModel):

    name = models.CharField(max_length=50)
    field_type = models.ForeignKey(FieldType, null=False, blank=False, default='', on_delete=models.CASCADE)
    options = ArrayField(models.CharField(max_length=200), blank=True, null=True)

    def __str__(self):
        return self.name


class RiskType(BaseModel):

    name = models.CharField(max_length=128)
    description = models.TextField()
    
    fields = models.ManyToManyField(Field)

    def __str__(self):
        return self.name
