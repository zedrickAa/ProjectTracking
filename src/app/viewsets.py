from rest_framework import viewsets
from .models import Location, Employee, Customer, Package
from .serializer import LocationSerializer, EmployeeSerializer, CustomerSerializer, PackageSerializer, Package2Serializer, Package4Serializer
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.filter(status = "Transito")
    serializer_class = PackageSerializer

class Package2ViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.filter(status = "Bodega")
    serializer_class = Package2Serializer

class Package3ViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.filter(status = "Entregado")
    serializer_class = Package2Serializer

class Package4ViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = Package4Serializer
    



