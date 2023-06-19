import csv
from typing import Set

from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: Set[Dish] = set()
        self._load_menu_data(source_path)

    def _load_menu_data(self, source_path: str):
        with open(source_path, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                dish_name, price, ingredient_name, quantity = row
                price = float(price)
                quantity = int(quantity)

                dish = self._create_dish_or_get(dish_name, price)
                Ingredient = self._create_ingredient_or_get(ingredient_name)
                dish.add_ingredient_dependency(Ingredient, quantity)

    def _create_dish_or_get(self, name: str, price: float) -> Dish:
        for dish in self.dishes:
            if dish.name == name:
                return dish
        new_dish = Dish(name, price)
        self.dishes.add(new_dish)
        return new_dish

    def _create_ingredient_or_get(self, name: str) -> Ingredient:
        return Ingredient(name)
