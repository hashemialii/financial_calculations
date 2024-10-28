from django.db import models


class ShahkarIncomeModel(models.Model):
    income = models.DecimalField(max_digits=50, decimal_places=2)
    year = models.IntegerField()
    month = models.IntegerField()

    def __str__(self):
        return f"Income: {self.income} | financial year and month: {self.year}-{self.month}"


class ShahkarBasicModel(models.Model):
    basic = models.OneToOneField(
        ShahkarIncomeModel, on_delete=models.CASCADE, related_name='shahkar_basic_model', null=True
    )
    year = models.IntegerField()
    month = models.IntegerField()
    amount = models.DecimalField(max_digits=50, decimal_places=2)

    class Meta:
        unique_together = ('year', 'month')
        ordering = ['year', 'month']

    def __str__(self):
        return f"year and month: {self.year}-{self.month} | amount: {self.amount} | {self.basic}"
