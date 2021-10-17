from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from tutorials.models import Departments, Product_Trees
from tutorials.serializers import DepartmentSerializer, ListTreesSerializer
# Create your views here.

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser


@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer, safe=False,  status=status.HTTP_200_OK)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False, status=status.HTTP_200_OK)
        return JsonResponse("Failed to Add", safe=False, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(
            DepartmentId=department_data['DepartmentId'])
        departments_serializer = DepartmentSerializer(
            department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully", safe=False, status=status.HTTP_200_OK)
        return JsonResponse("Failed to Update", status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False, status=status.HTTP_200_OK)


@csrf_exempt
def productsTreesApi(request, id=0):
    if request.method == 'GET':
        list = Product_Trees.objects.all()
        list_trees = ListTreesSerializer(list, many=True)
        return JsonResponse(list_trees.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        tree_data = JSONParser().parse(request)
        tree_serializer = ListTreesSerializer(data=tree_data)
        if tree_serializer.is_valid():
            tree_serializer.save()
            return JsonResponse({
                "massage": "Added Successfully Product Tree",
                "data": tree_serializer.data
            }, safe=False, status=status.HTTP_200_OK)
        return JsonResponse({
            "massage": "Failed to Add Product Tree",
        }, safe=False, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item = Product_Trees.objects.get(TreeId=id)
        item.delete()
        return JsonResponse({"massage": "Deleted Successfully"}, safe=False, status=status.HTTP_200_OK)
