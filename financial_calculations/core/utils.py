class FiscalYearCalculator:
    """
    A class to handle fiscal year calculations.
    """

    @staticmethod
    def calculate_fiscal_year(year, month):
        if month < 10:
            return year, month + 3
        else:
            return year + 1, month - 9
