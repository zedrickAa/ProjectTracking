from rest_framework import routers
from app.viewsets import LocationViewSet, EmployeeViewSet, CustomerViewSet, PackageViewSet, Package2ViewSet, Package3ViewSet,Package4ViewSet
router = routers.DefaultRouter()
router.register(r'app', LocationViewSet)
router.register(r'package3',  Package3ViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'package2',  Package2ViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'package',  PackageViewSet)
router.register(r'package4',  Package4ViewSet)
