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
from rest_framework.exceptions import NotFound
from .models import ShahkarModelBasic, ShahkarModelIncome
from .serializers import IncomeSerializer
from .services import IncomeService


class IncomeCalculationsViewSet(viewsets.ModelViewSet):
    queryset = ShahkarModelIncome.objects.all()
    serializer_class = IncomeSerializer

    def list(self, request, *args, **kwargs):
        """
        Override the list method to return a summary of all records.
        """
        queryset = self.get_queryset()
        summary = [
            {
                'id': income.basic.id,
                'year': income.basic.year,
                'month': income.basic.month,
                'amount': income.basic.amount
            }
            for income in queryset
        ]
        return Response(summary, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve the detailed information for a specific record.
        """
        instance = self.get_object()
        serializer = IncomeSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

    def update(self, request, *args, **kwargs):
        """
        Update an existing income calculation entry.
        """
        instance = self.get_object()
        amount = request.data.get('amount')

        if amount is None:
            return Response({'error': 'Please provide amount.'}, status=status.HTTP_400_BAD_REQUEST)

        # به‌روزرسانی مقدار
        instance.basic.amount = amount
        instance.basic.save()

        serializer = IncomeSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        """
        Delete an existing income calculation entry.
        """
        instance = self.get_object()
        instance.basic.delete()  # حذف رکورد پایه
        instance.delete()  # حذف رکورد درآمد

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        """
        Retrieve the object based on the URL parameter <id>.
        """
        try:
            # دریافت شناسه از URL
            id = self.kwargs['pk']
            # پیدا کردن ShahkarModelBasic بر اساس شناسه
            basic_instance = ShahkarModelBasic.objects.get(id=id)
            # پیدا کردن ShahkarModelIncome مربوط به این basic_instance
            return ShahkarModelIncome.objects.get(basic=basic_instance)
        except ShahkarModelBasic.DoesNotExist:
            raise NotFound("ShahkarModelBasic not found.")
        except ShahkarModelIncome.DoesNotExist:
            raise NotFound("ShahkarModelIncome not found.")



