from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, verbose_name="Name")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Description")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    categories = [('food', 'Food'), ('drink', 'Drink'), ('chocolate', 'Chocolate')]
    category = models.CharField(choices=categories, max_length=50, null=False, blank=False, default="food",
                                verbose_name="Category")

    def __str__(self):
        return self.category


class Good(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_goods")
    name = models.CharField(max_length=150, null=False, blank=False, verbose_name="Name")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="goods",
                                 verbose_name="Category")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

