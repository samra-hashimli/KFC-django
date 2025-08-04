from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Menu(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()
    stock = models.IntegerField(null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.stock})"
