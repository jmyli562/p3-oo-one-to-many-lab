class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner="John"):
        self.name = name
        self.owner = owner

        if pet_type not in Pet.PET_TYPES:
            raise Exception("Please use a valid pet type")
        else:
            self.pet_type = pet_type

        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet passed is not a Pet object")
        pet.owner = self

    def get_sorted_pets(self):
        owners_pet = sorted(
            [pet for pet in Pet.all if pet.owner == self], key=lambda x: x.name
        )

        return owners_pet
