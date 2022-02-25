from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255, blank=True)
    pizzas = models.ManyToManyField("restaurants.Pizza", related_name="restaurants")


class Pizza(models.Model):
    price = models.FloatField()
    is_vegetarian = models.BooleanField(default=False)
    toppings = models.ManyToManyField("restaurants.Topping", related_name="pizzas")


class Topping(models.Model):
    name = models.CharField(max_length=255, blank=False)


class PizzaFestival(models.Model):
    restaurant = models.ForeignKey(
        "restaurants.Restaurant", related_name="pizza_festivals", on_delete=models.CASCADE
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
