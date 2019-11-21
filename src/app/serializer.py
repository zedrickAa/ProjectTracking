from rest_framework import serializers
from .models import Location, Employee, Customer, Package
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

class Package2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

class Package4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
        depth = 2
        
     

