from rest_framework import serializers

from groups.models import Group, Element
from groups.models import check_image


class FilterElementsSerializer(serializers.ListSerializer):

    def to_representation(self, value):
        
        value = value.filter(checked=True)
        return super(FilterElementsSerializer, self).to_representation(value)


class ElementSerializer(serializers.ModelSerializer):

    def validate_picture(self, picture):
        
        check_image(picture)
        return picture

    class Meta:
        list_serializer_class = FilterElementsSerializer
        model = Element 
        exclude = ('checked',)


class GroupSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='groups-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Group 
        fields = '__all__'


class GroupListSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='groups-detail',
        lookup_field='pk'
    )

    elements = ElementSerializer(
        many=True,
        read_only=True,
    )

    groups = GroupSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Group 
        fields = '__all__'
