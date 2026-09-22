from django.db import models

from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    def total_price(self):
        return sum( item.total_price()
            for item in self.items.all()
    )

    def __str__(self):
        return f"{self.user.username}'s Cart"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):

        return self.product.price * self.quantity


    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
