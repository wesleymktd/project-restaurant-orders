from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
from src.models.ingredient import Restriction
import pytest


# Req 2
def test_dish():
    dish1 = Dish("lasanha presunto", 25.90)
    dish2 = Dish("lasanha presunto", 25.90)
    dish3 = Dish("pizza margarita", 50.50)

    ingredient1 = Ingredient("queijo gorgonzola")
    ingredient2 = Ingredient("creme de leite")
    # instanciação dish
    assert dish1.name == "lasanha presunto"
    assert dish1.name != "pizza peperone"
    with pytest.raises(TypeError):
        Dish("pizza", "abc")
    with pytest.raises(ValueError):
        Dish("pizza", -20.50)
    # __hash__
    assert hash(dish1) != hash(dish3)
    assert hash(dish1) == hash(dish2)
    # __eq__
    assert dish1 != dish3
    assert dish1 == dish2
    # __repr__
    assert repr(dish1) == "Dish('lasanha presunto', R$25.90)"
    # acesso a um valor do atributo recipe
    dish1.add_ingredient_dependency(ingredient1, 2)
    dish1.add_ingredient_dependency(ingredient2, 3)
    assert dish1.recipe.get(ingredient1) == 2
    # testando get_restrictions
    restrictions = dish1.get_restrictions()
    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert restrictions == expected_restrictions
    # testando get_ingredients
    ingredients = dish1.get_ingredients()
    expected_ingredients = {ingredient1, ingredient2}
    assert ingredients == expected_ingredients
