from rest_framework import serializers
from main.models import Lecture

class LectureSerializer(serializers.Serializer):
    name = serializers.CharField()
    code = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Lecture
        fields = ["id", "name", "code", "description"]

    def create(self, validated_data):
        return Lecture(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.code = validated_data.get("code", instance.code)
        instance.description = validated_data.get("description", instance.description)