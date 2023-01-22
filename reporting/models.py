from django.db import models

# Create your models here.
class Trade(models.Model): 
    class Side(models.IntegerChoices):
        BUY = 0, "Buy"
        SELL = 1, "Sell"

    class Order(models.IntegerChoices):
        LIMIT = 0, "Limit"
        MARKET = 1, "Market"

    class Market(models.IntegerChoices):
        SPOT = 0, "Spot"
        FUTURES = 1, "Futures"

    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    contract = models.CharField(max_length=10)
    side = models.PositiveSmallIntegerField(choices=Side.choices)
    filled_amount = models.IntegerField()
    fill_price = models.DecimalField(decimal_places=6, max_digits=8)
    value = models.DecimalField(decimal_places=2, max_digits=8)
    fee = models.DecimalField(decimal_places=2, max_digits=5)
    order = models.PositiveSmallIntegerField(choices=Order.choices)
    market = models.PositiveSmallIntegerField(choices=Market.choices)
    transaction_id = models.CharField(primary_key=True, unique=True, max_length=24)

    def __str__(self):
        return f"{self.transaction_id} - {self.contract}"