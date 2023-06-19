from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("queijo gorgonzola")
    expected_restriction1 = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    ingredient2 = Ingredient("banana")
    ingredient3 = Ingredient("banana")
    expected_restriction2 = set()
    # test instanciação
    assert ingredient1.name == "queijo gorgonzola"
    # test restrictions
    assert ingredient1.restrictions == expected_restriction1
    assert ingredient2.restrictions == expected_restriction2
    # test __repr__
    assert repr(ingredient1) == "Ingredient('queijo gorgonzola')"
    # test __eq__
    assert ingredient1 != ingredient2
    assert ingredient2 == ingredient3
    # test __hash__
    assert hash(ingredient1) != hash(ingredient3)
    assert hash(ingredient2) == hash(ingredient3)
