from rest_framework import serializers

class MovieSerializers(serializers.Serializer):
    id= serializers.IntegerField()
    titulo=serializers.CharField(max_length=200)

    