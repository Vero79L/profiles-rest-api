from rest_framework import serializers

class HelloSerializer(serializers.Serializer): #the 2nd 'Serializer' is a class name so it starts as Capital.
    """Serializers a name filed for testing our APIView"""
    name = serializers.CharField(max_length=10)
