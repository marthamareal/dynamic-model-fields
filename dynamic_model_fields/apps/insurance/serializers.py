from rest_framework import serializers

from .models import RiskType, Field, FieldType


class FieldTypeSerializer(serializers.ModelSerializer):
    """ Serializer class for Field Types"""

    name = serializers.CharField(required=True)
    
    class Meta:
        model = FieldType
        fields = ('id', 'name')

        read_only_fields = ['id', ]


class FieldSerializer(serializers.ModelSerializer):
    """ Serializer class for Fields"""

    name = serializers.CharField(required=True)
    field_type = serializers.UUIDField()

    options = serializers.ListField(required=False)

    class Meta:
        model = RiskType
        fields = ('id', 'name', 'field_type', 'options')

        read_only_fields = ['id', ]
    
    def validate_field_type(self, field_type):
        """ Validates field types data
        Args:
            field_type(uuid): Id for field type
        Returns:
            field_type(uuid): Id for field type if its valid
        Raises:
            ValidationError: If field type provided does not exist
        """

        try:
            field_type = FieldType.objects.get(id=field_type)
            return field_type

        except FieldType.DoesNotExist:
            raise serializers.ValidationError("Field type with id {} is not found".format(str(field_type)))


class RiskTypeSerializer(serializers.ModelSerializer):
    """ Serializer class for Risk Types"""

    fields = FieldSerializer(many=True, )

    class Meta:
        model = RiskType
        fields = ('id', 'name', 'description', 'fields')

        read_only_fields = ['id', ]

    def validate_fields(self, fields):
        """ Validates fields data
        Args:
            fields(list): list of fields
        Returns:
            fields(list): list of fields
        Raises:
            ValidationError: If no fields provided.
        """

        if fields == []:
            raise serializers.ValidationError("fields can not be empty")

        return fields
    
    def create(self, validated_data):
        """ Creates a risk type from the data provided
        Args:
            validated_data(dict): a dictionary of validated data of a risk type to create
        Returns:
            risk_type(object): Risk type object created
        """

        fields = validated_data.pop('fields',[]) # Separate fields from validated_data
        risk_type = RiskType.objects.create(**validated_data)

        self.add_fields(risk_type, fields)

        return risk_type

    def update(self, instance, validated_data):
        """ Updates a risk type from the data provided
        Args:
            instance(object): Risk type object updated
            validated_data(dict): a dictionary of validated data of a risk type to create
        Returns:
            risk_type(object): Risk type object updated
        """

        fields = validated_data.pop('fields',[])
        risk_type = super().update(instance, validated_data)

        self.add_fields(risk_type, fields)
        return risk_type
        
    
    def add_fields(self, risk_type, fields_list):
        """ Creates fields objects for a risk type
        Args:
            risk_type(object): Risk type object
            fields_list(list): list of fields
        """

        for field in fields_list:
            try:
                field = Field.objects.get(**field)
                risk_type.fields.add(field.id)

            except Field.DoesNotExist:
                risk_type.fields.create(**field)
