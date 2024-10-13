from .models import ShahkarModelBasic, ShahkarModelIncome
from core.utils import FiscalYearCalculator


# IncomeCalculatorService
class IncomeCalculator:
    """
    A class to calculate income based on the fiscal year multiplier.
    """

    multipliers = {
        1400: 10,
        1401: 100,
        1402: 1000,
        1403: 10000,
    }

    @classmethod
    def calculate(cls, year_2, amount):
        """
        Calculate income using the multiplier for the given year.
        """
        return amount * cls.multipliers.get(year_2, 0)


class IncomeService:
    """
    A service class to manage income creation and updates.
    """

    @staticmethod
    def create_basic_entry(data):
        basic_instance = ShahkarModelBasic.objects.create(
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

        income_instance = ShahkarModelIncome.objects.create(
            basic=basic_instance,
            income=income_amount,
            year_2=fiscal_year,
            month_2=fiscal_month
        )
        return income_instance

    @staticmethod
    def update_income(instance, data):
        fiscal_year, fiscal_month = FiscalYearCalculator.calculate_fiscal_year(
            data.get('year'), data.get('month')
        )
        new_income = IncomeCalculator.calculate(fiscal_year, data.get('amount'))

        instance.basic.year = data.get('year')
        instance.basic.month = data.get('month')
        instance.basic.amount = data.get('amount')
        instance.basic.save()

        instance.income = new_income
        instance.year_2 = fiscal_year
        instance.month_2 = fiscal_month
        instance.save()
        return instance
