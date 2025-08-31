class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"{pet_type} is not a valid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # Return all pets where pet.owner is this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, name, pet_type):
        return Pet(name, pet_type, self)

    def get_sorted_pets(self):
        # Return owner's pets sorted by pet name
        return sorted(self.pets(), key=lambda pet: pet.name)
