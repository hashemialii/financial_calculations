from django.db import models


# shahkar base model
class ShahkarModelBasic(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    month = models.IntegerField()
    amount = models.DecimalField(max_digits=50, decimal_places=2)

    class Meta:
        unique_together = ('year', 'month')

    def __str__(self):
        return f"{self.year}-{self.month} | Amount: {self.amount}"


class ShahkarModelIncome(models.Model):
    basic = models.OneToOneField(
        ShahkarModelBasic, on_delete=models.CASCADE, related_name='shahkar_income_details', primary_key=True
    )
    income = models.DecimalField(max_digits=50, decimal_places=2)
    year_2 = models.IntegerField(null=True, blank=True)
    month_2 = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Income: {self.income} | {self.year_2}-{self.month_2}"
