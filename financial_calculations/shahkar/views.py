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

        # basic_instance = IncomeService.create_basic_entry(request.data)
        basic_instance = IncomeService.create_basic_entry(serializer.validated_data)

        income_instance = IncomeService.create_income_entry(basic_instance)

        basic_instance.basic = income_instance
        basic_instance.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        basic_instance = IncomeService.update_basic_entry(instance, serializer.validated_data)

        income_instance = IncomeService.update_income_entry(basic_instance)

        basic_instance.basic = income_instance
        basic_instance.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
