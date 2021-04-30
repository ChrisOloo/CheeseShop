import pytest

from ..models import Cheese

# connecting our tests to our databases
pytestmark = pytest.mark.django_db

def test__str__():
    cheese = Cheese.objects.create(
        name = "Strepochinno",
        description = "The finnest cheese in Baganda. Should be your option one",
        firmness = Cheese.Firmness.HARD,
    )

    assert cheese.__str__() == "Strepochinno"
    assert str(cheese) == "Strepochinno"



