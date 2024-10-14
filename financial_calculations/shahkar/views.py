# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from .models import ShahkarModelBasic, ShahkarModelIncome
# from .serializers import BasicSerializer, IncomeSerializer
# from .services import IncomeService
#
#
# # self.getserializer
# # class IncomeViewSet(viewsets.ModelViewSet):
# class IncomeViewSet(viewsets.ViewSet):
#     # serializer_class = IncomeSerializer
#     # def perform_create(self, serializer):
#     #     smb = super().perform_create(serializer)
#     #     smb.save()
#
#     def create(self, request):
#         basic_data = request.data
#         basic_instance = IncomeService.create_basic_entry(basic_data)
#         income_instance = IncomeService.create_income_entry(basic_instance)
#         serializer = IncomeSerializer(income_instance)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
# # self.get_opject for viewset
#     def update(self, request, pk=None):
#         try:
#             instance = ShahkarModelIncome.objects.get(pk=pk)
#         except ShahkarModelIncome.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         updated_instance = IncomeService.update_income(instance, request.data)
#         serializer = IncomeSerializer(updated_instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def list(self, request):
#         queryset = ShahkarModelIncome.objects.all()
#         serializer = IncomeSerializer(queryset, many=True)
#         return Response(serializer.data)

from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import ShahkarModelBasic, ShahkarModelIncome
from .serializers import IncomeSerializer
from .services import IncomeService


class IncomeCalculationsViewSet(viewsets.ModelViewSet):
    queryset = ShahkarModelIncome.objects.all()
    serializer_class = IncomeSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new income calculation entry.
        """
        year = request.data.get('year')
        month = request.data.get('month')
        amount = request.data.get('amount')

        if year is None or month is None or amount is None:
            return Response({'error': 'Please provide year, month, and amount.'}, status=status.HTTP_400_BAD_REQUEST)

        basic_data = {
            'year': year,
            'month': month,
            'amount': amount
        }
        basic_instance = IncomeService.create_basic_entry(basic_data)
        income_instance = IncomeService.create_income_entry(basic_instance)

        serializer = IncomeSerializer(income_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        income_instance = self.get_object()
        basic_instance = income_instance.basic
        basic_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def update(self, request, *args, **kwargs):
    #     income_instance = self.get_object()
    #     basic_instance = income_instance.basic
    #     amount = request.data.get('amount')
    #     if amount is not None:
    #         basic_instance.amount = amount
    #         basic_instance.save()
    #         income_instance.amount = amount
    #         income_instance.save()
    #         serializer = IncomeSerializer(income_instance)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #     return Response({'error': 'Please provide the amount to update.'}, status=status.HTTP_400_BAD_REQUEST)
