class FiscalYearCalculator:
    """
    A class to handle fiscal year calculations.
    """

    @staticmethod
    def calculate_fiscal_year(year, month):
        """
        Calculate the fiscal year and month.
        """
        if month >= 4:
            return year, month
        return year - 1, month
