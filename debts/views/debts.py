from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from debts.models import DebtModel, UserModel
from debts.serializers import DebtSerializer


@api_view(['GET', 'POST'])
def debt_list_create(request):
    if request.method == 'GET':
        debts = DebtModel.objects.all()
        serializer = DebtSerializer(debts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = DebtSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def debt_detail(request, pk):
    debt = get_object_or_404(DebtModel, pk=pk)
    if request.method == 'GET':
        serializer = DebtSerializer(debt)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DebtSerializer(instance=debt, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = DebtSerializer(instance=debt, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        debt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
