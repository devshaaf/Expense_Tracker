from django.shortcuts import render, get_object_or_404
from .serializers import ExpenseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from expense.models import Expense
from .filters import ExpenseFilter
from django.db.models import Sum
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

# for listing expenses and filtering by category
@swagger_auto_schema(
    method='get',
    operation_description="Get all expenses for authenticated user with optional category filtering",
    manual_parameters=[
        openapi.Parameter('category', openapi.IN_QUERY, description="Filter by category", type=openapi.TYPE_STRING)
    ]
)
# for adding expenses
@swagger_auto_schema(
    method='post',
    operation_description="Create a new expense",
    request_body=ExpenseSerializer
)

@api_view(['GET', 'POST'])
def Expenses(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            queryset = Expense.objects.filter(User_ID=request.user)
            expense_filter = ExpenseFilter(queryset=queryset, data=request.GET)
            final_queryset = expense_filter.qs # this .qs attribute has filtered queryset
            serializer = ExpenseSerializer(final_queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = ExpenseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(User_ID=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(
    method='get',
    operation_description="Get a specific expense by ID"
)
@swagger_auto_schema(
    method='put',
    operation_description="Update a specific expense",
    request_body=ExpenseSerializer
)
@swagger_auto_schema(
    method='delete',
    operation_description="Delete a specific expense"
)


@api_view(['GET', 'PUT', 'DELETE'])
def ExpenseDetail(request, pk):
    expense = get_object_or_404(Expense, pk=pk, User_ID=request.user)
    if request.user.is_authenticated:
        if request.method == 'PUT':
            serializer = ExpenseSerializer(data=request.data, instance=expense)
            if serializer.is_valid():
                serializer.save(User_ID=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'GET':
            serializer = ExpenseSerializer(expense)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            expense.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(
    method='get',
    operation_description="Get total spending summary with overall and category-wise breakdown"
)

@api_view(['GET'])
def TotalSpend(request):
    if not request.user.is_authenticated:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    else:
        overall_spendings = Expense.objects.filter(User_ID=request.user).aggregate(overall_spendings=Sum('amount'))
        spendings_by_category = Expense.objects.filter(User_ID=request.user).values('category').annotate(total=Sum('amount'))
        response_data = {
            'overall_spendings': overall_spendings['overall_spendings'] or 0,
            'spendings_by_category': list(spendings_by_category)
        }
        return Response(response_data, status=status.HTTP_200_OK)