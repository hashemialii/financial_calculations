from .models import ShahkarBasicModel, ShahkarIncomeModel
from core.utils import FiscalYearCalculator


class IncomeCalculator:
    multipliers = {
        1400: 10,
        1401: 100,
        1402: 1000,
        1403: 10000,
    }

    @classmethod
    def calculate(cls, year, amount):
        return amount * cls.multipliers.get(year, 0)


class IncomeService:
    @staticmethod
    def create_basic_entry(data):
        basic_instance = ShahkarBasicModel.objects.create(
            year=data.get('year'),
            month=data.get('month'),
            amount=data.get('amount')
        )
        return basic_instance

    @staticmethod
    def create_income_entry(basic_instance):
        fiscal_year, fiscal_month = FiscalYearCalculator.calculate_fiscal_year(
            basic_instance.year, basic_instance.month
        )
        income_amount = IncomeCalculator.calculate(fiscal_year, basic_instance.amount)

        income_instance = ShahkarIncomeModel.objects.create(
            income=income_amount,
            year=fiscal_year,
            month=fiscal_month
        )
        return income_instance


    # @staticmethod
    # def update_amount(income_instance, new_amount):
    #     income_instance.basic.amount = new_amount
    #     income_instance.basic.save()
    #     fiscal_year, fiscal_month = income_instance.year, income_instance.month
    #
    #     new_income = IncomeCalculator.calculate(fiscal_year, new_amount)
    #     income_instance.income = new_income
    #     income_instance.save()
    #     return income_instance
