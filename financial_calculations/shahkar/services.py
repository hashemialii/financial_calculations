from .models import ShahkarBasicModel, ShahkarIncomeModel
from core.utils import FiscalYearCalculator


class IncomeCalculator:
    @classmethod
    def get_multipliers(cls):
        return {
            1400: 10,
            1401: 100,
            1402: 1000,
            1403: 10000,
        }

    @classmethod
    def calculate(cls, year, amount):
        multipliers = cls.get_multipliers()
        return amount * multipliers.get(year, 0)


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

    @staticmethod
    def update_basic_entry(basic_instance, data):
        basic_instance.year = data.get('year', basic_instance.year)
        basic_instance.month = data.get('month', basic_instance.month)
        basic_instance.amount = data.get('amount', basic_instance.amount)
        basic_instance.save()
        return basic_instance

    @staticmethod
    def update_income_entry(basic_instance):
        income_instance = basic_instance.basic
        income_instance.income = IncomeCalculator.calculate(
            basic_instance.year, basic_instance.amount
        )
        income_instance.save()
        return income_instance
