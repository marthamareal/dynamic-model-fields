from django.contrib import admin
from .models import Field, FieldType, RiskType

admin.site.register(Field)
admin.site.register(FieldType)
admin.site.register(RiskType)
