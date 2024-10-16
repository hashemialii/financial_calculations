from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import ShahkarModelIncome
from .serializers import IncomeSerializer
from .services import IncomeService


class IncomeCalculationsViewSet(viewsets.ModelViewSet):
    queryset = ShahkarModelIncome.objects.all()
    serializer_class = IncomeSerializer

    def create(self, request, *args, **kwargs):
        required_fields = ['year', 'month', 'amount']

        if not all(field in request.data for field in required_fields):
            return Response(
                {'error': 'Please provide year, month, and amount.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if len(request.data) != len(required_fields):
            return Response(
                {'error': 'Only year, month, and amount fields are allowed.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        print(request.data)
        basic_instance = IncomeService.create_basic_entry(request.data)
        print(basic_instance)
        income_instance = IncomeService.create_income_entry(basic_instance)
        print(income_instance)
        serializer = self.get_serializer(income_instance)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        print(request.data)
        income_instance = self.get_object()
        print(income_instance)
        amount = request.data.get('amount')
        if amount is None:
            return Response({'error': 'Amount is required.'}, status=status.HTTP_400_BAD_REQUEST)
        updated_instance = IncomeService.update_amount(income_instance, amount)
        serializer = self.get_serializer(updated_instance)
        print(serializer.data)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        income_instance = self.get_object()
        basic_instance = income_instance.basic
        basic_instance.delete()
        return Response({f'{income_instance.basic} was deleted'})
