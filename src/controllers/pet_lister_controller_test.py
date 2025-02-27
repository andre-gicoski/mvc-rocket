from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetsListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Fluffy", type="Cat", id=1),
            PetsTable(name="Buddy", type="Dog", id=17),
        ]

def test_list_pets():
    controller = PetsListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
           "data": {
                "type": "Pets",
                "count": 2,
                "attributes": [
                    {"name": "Fluffy", "id": 1 },
                    {"name": "Buddy", "id": 17 }
                ]
            }
        }

    assert response == expected_response
