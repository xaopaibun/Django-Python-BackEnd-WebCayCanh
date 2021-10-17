from rest_framework import serializers
from tutorials.models import Departments, Product_Trees


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId', 'DepartmentName')


class ListTreesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Trees
        fields = ('TreeId', 'TreeName', 'TreePrice', 'TreeImage', 'TreeQuantity', 'TreeContent','TreeCreateAt', 'TreeUpdateAt')
