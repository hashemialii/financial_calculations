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

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ShahkarModelBasic, ShahkarModelIncome
from .serializers import IncomeSerializer
from .services import IncomeService


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = ShahkarModelIncome.objects.all()
    serializer_class = IncomeSerializer

    def create(self, request, *args, **kwargs):
        basic_data = request.data
        basic_instance = IncomeService.create_basic_entry(basic_data)
        income_instance = IncomeService.create_income_entry(basic_instance)
        serializer = self.get_serializer(income_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        year = request.data.get('year')
        month = request.data.get('month')

        # جستجوی نمونه با استفاده از سال و ماه
        try:
            instance = self.queryset.get(year=year, month=month)
        except ShahkarModelIncome.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # بروزرسانی نمونه
        updated_instance = IncomeService.update_income(instance, request.data)
        serializer = self.get_serializer(updated_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
