from rest_framework import serializers
from poststation.models import ShoujiPoststation

class PoststationSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    cat_id = serializers.IntegerField()
    attr_name = serializers.CharField(max_length=255,allow_blank=True)
    attr_input_type = serializers.IntegerField()
    attr_type = serializers.IntegerField()
    attr_values = serializers.CharField(max_length=255,allow_blank=True)
    attr_index = serializers.IntegerField()
    sort_order = serializers.IntegerField()
    is_linked = serializers.IntegerField()
    attr_group = serializers.IntegerField()
    province = serializers.CharField(max_length=60, allow_blank=True, allow_null=True)
    city = serializers.CharField(max_length=60, allow_blank=True, allow_null=True)
    tel = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    addr = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    longitude = serializers.CharField(max_length=32, allow_blank=True, allow_null=True)
    latitude = serializers.CharField(max_length=32, allow_blank=True, allow_null=True)

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return ShoujiPoststation.objects.create(**validated_data)


    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance