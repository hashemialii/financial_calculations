from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import ShahkarBasicModel
from .serializers import BasicSerializer
from .services import IncomeService


class IncomeCalculationsViewSet(viewsets.ModelViewSet):
    queryset = ShahkarBasicModel.objects.all()
    serializer_class = BasicSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        basic_instance = IncomeService.create_basic_entry(request.data)

        IncomeService.create_income_entry(basic_instance)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        print(request.data)
        income_instance = self.get_object()
        print(income_instance)
        amount = request.data.get('amount')
        # partial update
        # upddate amoynt only
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
