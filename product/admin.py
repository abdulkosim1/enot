from django.contrib import admin
from .models import Product, Rating, Comment, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Category)