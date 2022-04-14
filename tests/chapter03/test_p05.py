from chapter03.p05 import AnimalShelterQueue, AnimalType, Animal


def test_animal_shelter():
    fluffy, catty, doggy = (
        Animal("Fluffy", AnimalType.DOG),
        Animal("Catty", AnimalType.CAT),
        Animal("Doggy", AnimalType.DOG),
    )

    shelter = AnimalShelterQueue()
    shelter.enqueue(fluffy)
    shelter.enqueue(catty)
    shelter.enqueue(doggy)

    assert shelter.pop_head() == fluffy


def test_animal_shelter_cat_first(shelter, cat):
    first_cat = shelter.dequeue_cat()
    assert first_cat == cat
