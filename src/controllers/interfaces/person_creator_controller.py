from abc import ABC, abstractmethod
from typing import Dict

@abstractmethod
class PersonCreatorControllerInterface(ABC):
    def create(self, person_info: Dict) -> Dict:
        pass
