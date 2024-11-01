from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from debts.models import UserModel, DebtModel
from debts.serializers import UserSerializer, DebtSerializer


@api_view(['GET', 'POST'])
def user_list_create(request):
    if request.method == 'GET':
        users = UserModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def user_detail(request, pk):
    user = get_object_or_404(UserModel, pk=pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def authenticated_view(request):
    return Response({'message': 'Authenticated_view'})


@api_view(['GET'])
@permission_classes([IsAdminUser])
def authenticated_super_user(request):
    user = request.user
    return Response({'message': f'Authenticated super user view {user.username}'})


@api_view(['GET'])
def unauthenticated_view(request):
    return Response({'message': 'Unauthenticated_view'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def debts_given(request):
    """View to list all debts given by the authenticated user."""
    user = request.user
    debts = DebtModel.objects.filter(giver=user)
    serializer = DebtSerializer(debts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def debts_received(request):
    user = request.user
    debts = DebtModel.objects.filter(receiver=user)
    serializer = DebtSerializer(debts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_user_debts(request):
    user = request.user
    given_debts = DebtModel.objects.filter(giver=user)
    received_debts = DebtModel.objects.filter(receiver=user)

    # Debugging outputs
    print("Given Debts:", given_debts)  # Check what's in given debts
    print("Received Debts:", received_debts)  # Check what's in received debts

    all_debts = given_debts | received_debts

    # More debugging output
    print("All Debts:", all_debts)  # Check combined debts

    serializer = DebtSerializer(all_debts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

