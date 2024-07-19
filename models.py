from django.db import models
from django.contrib.auth.models import User

class FoodItem(models.Model):
    name = models.CharField(max_length=100)  # Name of the food item
    description = models.TextField()  # Detailed description
    image = models.ImageField(upload_to='food_images/')  # Image of the food item
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)  # User who submitted the item

    def __str__(self):
        return self.name

class RecipeDetail(models.Model):
    food_item = models.OneToOneField(FoodItem, related_name='recipe_detail', on_delete=models.CASCADE)  # Link to FoodItem
    ingredients = models.TextField()  # Ingredients for the recipe
    how_to_make = models.TextField()  # Instructions on how to make the recipe

    def __str__(self):
        return f"Recipe for {self.food_item.name}"

    @property
    def recipe_image(self):
        # Return the URL of the recipe image if available
        return self.food_item.image.url if self.food_item.image else None

    @property
    def food_item_name(self):
        # Return the name of the food item
        return self.food_item.name
