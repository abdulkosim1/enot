from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

# from post.models import User

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products'
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_categories', default=1)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    images = models.ImageField(upload_to='product_images/')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.name} {self.owner}'

class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_ratings')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_ratings')
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.owner} --> {self.product.name}'

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.owner} --> {self.product.name}'
    
# class Favorite(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorives')
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favorites')

#     def __str__(self) -> str:
#         return f'{self.owner_id} --- {self.post_id}'