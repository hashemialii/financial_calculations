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

    def retrieve(self, request, *args, **kwargs):
        year = request.data.get('year')
        month = request.data.get('month')

        if year is None or month is None:
            return Response({'error': 'Please provide year and month.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = ShahkarModelIncome.objects.get(basic__year=year, basic__month=month)
            serializer = IncomeSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ShahkarModelIncome.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        year = request.data.get('year')
        month = request.data.get('month')

        if year is None or month is None:
            return Response({'error': 'Please provide year and month.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # پیدا کردن رکورد پایه بر اساس سال و ماه
            basic_instance = ShahkarModelBasic.objects.get(year=year, month=month)
            id1 = basic_instance.id

            # استفاده از basic_id برای حذف رکورد درآمد
            income_instance = ShahkarModelIncome.objects.get(basic_id=id1)

            # حذف رکورد درآمد
            income_instance.delete()

            # حذف رکورد پایه
            basic_instance.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except ShahkarModelBasic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ShahkarModelIncome.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        year = request.data.get('year')
        month = request.data.get('month')
        amount = request.data.get('amount')

        if year is None or month is None or amount is None:
            return Response({'error': 'Please provide year, month, and amount.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = ShahkarModelIncome.objects.get(basic__year=year, basic__month=month)
            data = {'year': year, 'month': month, 'amount': amount}
            updated_instance = IncomeService.update_income(instance, data)
            serializer = IncomeSerializer(updated_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ShahkarModelIncome.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
