from abc import ABC, abstractmethod

@abstractmethod
class PetDeleterControllerInterface(ABC):

    def delete(self, name: str) -> None:
        pass
