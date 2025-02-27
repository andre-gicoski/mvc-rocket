from typing import List, Dict
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable
from .interfaces.pet_lister_controller import PetsListerControllerInterface


class PetsListerController(PetsListerControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def list(self) -> Dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response

    def __get_pets_in_db(self) -> List[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets

    def __format_response(self, pets: List[PetsTable]) -> Dict:
        formated_pets = []
        for pet in pets:
            formated_pets.append({"name": pet.name, "id": pet.id})

        return {
            "data": {
                "type": "Pets",
                "count": len(formated_pets),
                "attributes": formated_pets
            }
        }
