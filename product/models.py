from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    images = models.ImageField(upload_to='product_images/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title} {self.owner}'

