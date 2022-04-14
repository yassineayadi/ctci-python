import pytest

from chapter03.p05 import Animal, AnimalShelterQueue, AnimalType


@pytest.fixture
def cat():
    cat = Animal("Catty", AnimalType.CAT)
    return cat


@pytest.fixture
def shelter(cat):
    fluffy, doggy = (
        Animal("Fluffy", AnimalType.DOG),
        Animal("Doggy", AnimalType.DOG),
    )
    shelter = AnimalShelterQueue()
    shelter.enqueue(fluffy)
    shelter.enqueue(cat)
    shelter.enqueue(doggy)
    return shelter
